# Database configuration
# - Use SQLAlchemy create_engine
# - For now, use SQLite for local dev
# - Later swap with Azure SQL connection string

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./wellogs.db")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
