
from sqlalchemy import create_engine, Column, Integer, String,Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey


# Vehicle path model
Base = declarative_base()

class VehiclePath(Base):
    __tablename__ = 'vehicle_path'
    id = Column(Integer, primary_key=True)
    track_id = Column(Integer, ForeignKey('vehicle.track_id'))
    lat = Column(Float)
    lon = Column(Float)
    speed =  Column(Float)
    lon_acc = Column(Float)
    lat_acc= Column(Float)
    time =Column(Float)

    vehicle = relationship("Vehicle", back_populates="vehicle_path")


# Vehicle path model
Base = declarative_base()

class Vehicle(Base):
    __tablename__ = 'vehicle'
    track_id = Column(Integer, primary_key=True)
    type = Column(String)
    traveled_d = Column(Float)
    avg_speed =  Column(Float)
    
    vehicle_path = relationship("VehiclePath", back_populates="vehicle")