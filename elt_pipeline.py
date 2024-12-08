from src.extract.extract import start_extract
from src.transform.transform import transformation
from src.load.load import load
from configuration.config import config


def main():

    try:
        print('extracting......')
        start_extract(config.api_weather,config.cities,config.unit,config.weather_url,config.data_weather)
        print('done')


        print('tarnsforming.......')
        transformation()
        print('done')


        print('loading.......')
        load()
        print('done')

    except Exception as e :
        print(f'erreur : {e}')



if __name__=='__main__':
    print('start etl')
    main()
    print('end etl')


