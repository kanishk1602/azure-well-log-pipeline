# Pytest tests for FastAPI backend
# - Test GET /health returns 200
# - Test GET /wells returns empty list initially
# - Test adding a sample Well + Log in DB and retrieving via /wells and /wells/{id}/logs

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from ..models import Base, Well, Log
from ..main import app, get_db

TEST_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(TEST_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

@pytest.fixture(scope="function", autouse=True)
def test_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_get_wells_empty():
    response = client.get("/wells")
    assert response.status_code == 200
    assert response.json() == []

def test_add_and_get_well_and_logs():
    # Add a well and log to the test database
    db = TestingSessionLocal()
    well = Well(name="Well1", location="Location1")
    db.add(well)
    db.commit()
    log = Log(well_id=well.id, depth=100.0, property="pressure", value=50.0)
    db.add(log)
    db.commit()
    well_id = well.id
    db.close()

    # Test GET /wells
    response = client.get("/wells")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["name"] == "Well1"
    assert data[0]["location"] == "Location1"

    # Test GET /wells/{id}/logs
    response = client.get(f"/wells/{well_id}/logs")
    assert response.status_code == 200
    logs = response.json()
    assert len(logs) == 1
    assert logs[0]["property"] == "pressure"
    assert logs[0]["value"] == 50.0
    assert logs[0]["depth"] == 100.0
