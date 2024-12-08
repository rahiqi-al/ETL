import yaml
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:

    config_file_path = os.path.join(os.path.dirname(__file__), 'config.yml')
    # Load values from config.yml
    with open(config_file_path, "r") as file:
        config_data = yaml.load(file , Loader=yaml.FullLoader)

    url = config_data["EXTRACT_PARAMS"]["URL"]
    n_p = config_data["EXTRACT_PARAMS"]["N_P"]
    category = config_data["EXTRACT_PARAMS"]["CATEGORY"]
    data = config_data["EXTRACT_PARAMS"]["DATA"]
    xpaths = config_data["EXTRACT_PARAMS"]["XPATHS"]
    cities = config_data["EXTRACT_PARAMS"]["CITIES"]
    unit = config_data["EXTRACT_PARAMS"]["UNITS"]
    weather_url = config_data["EXTRACT_PARAMS"]["WEATHER_URL"]
    data_weather = config_data["EXTRACT_PARAMS"]["DATA_WEATHER"]
    path_wheather = config_data["TRANSFORM_PARAMS"]["PATH_WHEATHER"]
    path_web = config_data["TRANSFORM_PARAMS"]["PATH_WEB"]
    path_weather_load = config_data["LOAD_PARAMS"]["PATH_WHEATHER"]
    path_web_load = config_data["LOAD_PARAMS"]["PATH_WEB"]




    api_weather = os.getenv('API_KEY_WEATHER')
    database_url = os.getenv('DATABASE_URL')
    


config = Config()


