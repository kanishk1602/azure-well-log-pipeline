# FastAPI backend for Welllog Data Pipeline
# Requirements:
# - Expose REST API endpoints:
#   GET /wells → list wells
#   GET /wells/{id}/logs?from=&to=&property= → return filtered logs
# - Use SQLAlchemy ORM for Azure SQL integration
# - Define models: Well (id, name, location), Log (id, well_id, depth, property, value, timestamp)
# - Include CORS middleware for Angular frontend
# - Add healthcheck endpoint GET /health

from fastapi import FastAPI, HTTPException, Depends, Query
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session, relationship
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
import os

# Database setup
DATABASE_URL = os.getenv("DATABASE_URL", "mssql+pyodbc://kanishk1602:Ashansa%401602@chevron.database.windows.net/wellogs?driver=ODBC+Driver+18+for+SQL+Server")  # Replace with actual Azure SQL connection string
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# SQLAlchemy Models
class Well(Base):
    __tablename__ = 'wells'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    location = Column(String(255))
    logs = relationship("Log", back_populates="well")

class Log(Base):
    __tablename__ = 'logs'
    id = Column(Integer, primary_key=True, index=True)
    well_id = Column(Integer, ForeignKey('wells.id'), index=True)
    depth = Column(Float)
    property = Column(String(255))
    value = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)
    well = relationship("Well", back_populates="logs")

# Create tables
Base.metadata.create_all(bind=engine)

# Pydantic Models
class WellResponse(BaseModel):
    id: int
    name: str
    location: str

class LogResponse(BaseModel):
    id: int
    well_id: int
    depth: float
    property: str
    value: float
    timestamp: datetime

# FastAPI App
app = FastAPI()

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust for production, e.g., ["http://localhost:4200"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoints
@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/wells", response_model=List[WellResponse])
def list_wells(db: Session = Depends(get_db)):
    wells = db.query(Well).all()
    return wells

@app.get("/wells/{well_id}/logs", response_model=List[LogResponse])
def get_logs(
    well_id: int,
    from_depth: Optional[float] = Query(None, alias="from"),
    to_depth: Optional[float] = Query(None, alias="to"),
    property_filter: Optional[str] = Query(None, alias="property"),
    db: Session = Depends(get_db)
):
    # Check if well exists
    well = db.query(Well).filter(Well.id == well_id).first()
    if not well:
        raise HTTPException(status_code=404, detail="Well not found")
    
    query = db.query(Log).filter(Log.well_id == well_id)
    if from_depth is not None:
        query = query.filter(Log.depth >= from_depth)
    if to_depth is not None:
        query = query.filter(Log.depth <= to_depth)
    if property_filter is not None:
        query = query.filter(Log.property == property_filter)
    
    logs = query.all()
    return logs

