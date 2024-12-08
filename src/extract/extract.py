import threading
from .houses_pets_business import scrap_hpb
from .weather_api import scrap_api
from configuration.config import config


def start_extract(api_key,cities_uk,unite,url_wea,wea_data):
    
    x = threading.Thread(target=scrap_hpb.scrap)
    y = threading.Thread(target=scrap_api, args=(api_key,cities_uk,unite,url_wea,wea_data))

    x.start()
    y.start()

    x.join()
    y.join()


#start_extract(config.api_weather,config.cities,config.unit,config.weather_url,config.data_weather)



