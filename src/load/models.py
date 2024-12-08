from sqlalchemy import  Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship



Base = declarative_base()


class Annonce(Base):
    __tablename__ = 'annonces'


    id_annonce = Column(Integer, primary_key = True)
    title = Column(String)
    price = Column(Integer)
    type_annonce = Column(String)
    ad_id = Column(Integer)
    description = Column(String)
    url = Column(String)
    id_city = Column(Integer, ForeignKey('cities.id_city'), nullable = False)

    cities_annonce = relationship('City', back_populates='annonces')

class City(Base):
    __tablename__ = 'cities'


    id_city = Column(Integer, primary_key= True)
    name = Column(String)

    annonces = relationship('Annonce' , back_populates = 'cities_annonce')
    weathers = relationship('Weather', back_populates = 'cities_weather')


class Weather(Base):
    __tablename__ = 'weathers'


    id_weather = Column(Integer, primary_key = True)
    temp = Column(Float)
    humidity = Column(Integer)
    description = Column(String)
    wind_speed = Column(Float)
    sunset_time = Column(DateTime)
    id_city = Column(Integer, ForeignKey('cities.id_city'), nullable = False)

    cities_weather = relationship('City', back_populates = 'weathers')


       
