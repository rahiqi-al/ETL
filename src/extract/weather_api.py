import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from configuration.config import config
import requests
import datetime as dt
import pandas as pd


def turn_to_csv(info,data_wea):
    for key, value in zip(data_wea.keys(),info):
        data_wea[key].append(value)
    



def scrap_api(api,cities,unit,base_url,data_wea):
    for city in cities:
        url = f"{base_url}q={city}&appid={api}&units={unit}"
        response = requests.get(url)
        if not response.ok :
            turn_to_csv([None]*6,data_wea)
            continue
            

        data = response.json()
        
        sunset_time = dt.datetime.fromtimestamp(data['sys']['sunset']+data['timezone'], tz=dt.timezone.utc).date().strftime("%Y-%m-%d")
        info = [city,data['main']['temp'],data['main']['humidity'],data['weather'][0]['description'],data['wind']['speed'],sunset_time]
        
        turn_to_csv(info,data_wea)
    df = pd.DataFrame(data_wea)
    output_dir = r'C:\Users\Youcode\ETL_project\data'
    os.makedirs(output_dir, exist_ok=True)
    df.to_csv(os.path.join(output_dir, 'extraction_wheather.csv'), encoding='utf-8', index=False)
    
       

