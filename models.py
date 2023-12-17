from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Float, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from config import Base


class BeachInfoModel(Base):
    __tablename__ = 'beach_info'

    id = Column(Integer, primary_key=True, index=True)
    area = Column(String)
    region = Column(String)
    beach = Column(String)
    temperature_wind = Column(Float)
    feels_like = Column(Float)
    temperature_water = Column(Float)
    rain_mm = Column(Integer)
    rain_chance = Column(Integer)
    snow_mm = Column(Integer)
    snow_chance = Column(Integer)
    wind_dir = Column(String)
    wind_speed = Column(Integer)
    wave_dir = Column(String)
    wave_height = Column(Float)
    wave_period = Column(Float)
    business = Column(Integer)
    business_hotspot = Column(Integer)
    flag = Column(String)
    life_guards = Column(Integer)
    sun_bed = Column(Integer)
    wc_distance = Column(Integer)
    dressing_room = Column(Integer)
    bar_restaurant = Column(Integer)
    recreation = Column(Integer)
    created_on = Column(DateTime)

class Users(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    disabled = Column(Boolean, default=True)   
