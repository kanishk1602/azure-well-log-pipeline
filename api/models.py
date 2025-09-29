# SQLAlchemy models for Well and Log tables
# Well: id (PK), name, location
# Log: id (PK), well_id (FK), depth, property, value, timestamp
# Use Base = declarative_base()
# Add __repr__ methods for debugging

from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

class Well(Base):
    __tablename__ = 'wells'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    location = Column(String(255))
    logs = relationship("Log", back_populates="well")

    def __repr__(self):
        return f"<Well(id={self.id}, name='{self.name}', location='{self.location}')>"

class Log(Base):
    __tablename__ = 'logs'
    id = Column(Integer, primary_key=True, index=True)
    well_id = Column(Integer, ForeignKey('wells.id'), index=True)
    depth = Column(Float)
    property = Column(String(255))
    value = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)
    well = relationship("Well", back_populates="logs")

    def __repr__(self):
        return f"<Log(id={self.id}, well_id={self.well_id}, depth={self.depth}, property='{self.property}', value={self.value}, timestamp={self.timestamp})>"
