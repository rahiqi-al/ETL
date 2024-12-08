import sys
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from configuration.config import config
import pandas as pd
from .models import Base,City,Annonce,Weather






def load():


    engine = create_engine(config.database_url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    

    


    df_weather = pd.read_csv(config.path_weather_load)
    df_web = pd.read_csv(config.path_web_load)

    try:
        for _,row in df_web.iterrows():

            ville = session.query(City).filter(City.name==row['localisation']).first()
            if not ville : 
                ville = City(name = row['localisation'])
                session.add(ville)
                
            
            annonce = Annonce(title=row['title'],
            price=row['price'],
            type_annonce=row['type_annonce'],
            ad_id=row['ad_id'],
            description=row['description'],
            url=row['url_annonce'],
            id_city=ville.id_city)
            
            session.add(annonce)
        
        session.commit()
        
        for _,row in df_weather.iterrows():

            ville = session.query(City).filter(City.name==row['localisation']).first()
            if not ville : 
                ville = City(name = row['localisation'])
                session.add(ville)
                
            
            weather = Weather(
                temp=row['temp'],
                humidity=row['humidity'],
                description=row['description'],
                wind_speed=row['wind_speed'],
                sunset_time=row['sunset_time'],
                id_city=ville.id_city)
            session.add(weather)
            
        session.commit()

    except Exception:
        session.rollback()
    

    finally:
      session.close()




#load()
