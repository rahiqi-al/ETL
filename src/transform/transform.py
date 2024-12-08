import pandas as pd 
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from configuration.config import config
#from sklearn.preprocessing import MinMaxScaler,StandardScaler


def handle_pets(df_pets):
    df_pets['price'] = df_pets['price'].str.replace(r'[£,]', '', regex=True)  
    df_pets['price'] = pd.to_numeric(df_pets['price'], errors='coerce') 
    if df_pets['price'].skew() > 0.5 or df_pets['price'].skew() < -0.5:
         df_pets['price'].fillna(df_pets['price'].median(), inplace=True)
    else:
        df_pets['price'].fillna(df_pets['price'].mean(), inplace=True)
    
    return df_pets



def handle_services(df_services):
    df_services['price'] = pd.to_numeric(df_services['price'], errors='coerce')
    #it become object and when we append them the type of prive become object not float
    #df_services['price'] = df_services['price'].apply(lambda x: "not provided" if pd.isna(x) else x)
    
    return df_services

def handle_property(df_property):
    df_property['price'] = df_property['price'].str.replace(r'[£,]', '', regex=True) 
    df_property['price'] = df_property['price'].str.replace(r'(pm|pw)', '', regex=True)
    df_property['price'] = pd.to_numeric(df_property['price'], errors='coerce') 
    if df_property['price'].skew() > 0.5 or df_property['price'].skew() < -0.5:
        df_property['price'].fillna(df_property['price'].median(), inplace=True)
    
    else:
        df_property['price'].fillna(df_property['price'].mean(), inplace=True)
    

    return df_property



def find_city(x, cities):
    for city in cities:
        if city in x:
            return city  
    return x

def trans_df_web(path):
    df = pd.read_csv(path)
    cities = ['London', 'Manchester', 'Birmingham', 'Liverpool', 'Leeds', 'Bristol', 'Sheffield', 'Glasgow', 'Edinburgh', 'Cardiff']
    df['localisation'] = df['localisation'].apply(find_city, cities=cities)
    df['ad_id'] = pd.to_numeric(df['ad_id'], errors='coerce') 


    df_pets = df[df['type_annonce']=='Pets']
    df_services = df[df['type_annonce']=='Services']
    df_property = df[df['type_annonce']=='Property']

    df_pets = handle_pets(df_pets)
    df_services = handle_services(df_services)
    df_property = handle_property(df_property)

    df=pd.concat([df_pets,df_property,df_services], ignore_index=True)

    output_dir = r'C:\Users\Youcode\ETL_project\data'
    os.makedirs(output_dir, exist_ok=True)
    df.to_csv(os.path.join(output_dir, 'transform_web.csv'), encoding='utf-8', index=False)




def trans_df_api(path):
    df = pd.read_csv(path)
    df['sunset_time']=pd.to_datetime(df['sunset_time'])
    #df[['temp', 'humidity' ]] = pd.DataFrame(MinMaxScaler().fit_transform(df[['temp', 'humidity' ]]))
    #df['wind_speed']= StandardScaler().fit_transform(df[['wind_speed']])
    output_dir = r'C:\Users\Youcode\ETL_project\data'
    os.makedirs(output_dir, exist_ok=True)
    df.to_csv(os.path.join(output_dir, 'transform_wheiter.csv'), encoding='utf-8', index=False)



def transformation():
    trans_df_web(config.path_web)
    trans_df_api(config.path_wheather)


#transformation()
