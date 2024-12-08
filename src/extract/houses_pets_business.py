from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import time
import pandas as pd
import itertools
import sys
import os
#  used to access modules(Python file) located in directories above the current script.
# it makes sure Python can find files from a higher-level folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from configuration.config import config


class Scrap_hpb:
    def __init__(self,driver,url,Np,data,category):
        self.driver = driver
        self.url = url
        self.Np = Np 
        self.data = data
        self.category = category
        self.lis = []
    

    def scrap_data(self,annonce):
        self.driver.get(annonce)
        time.sleep(2)
        ld = []

        for i in config.xpaths['data_annonce']  :
            try:
                ld.append(self.driver.find_element(By.XPATH,i).text)

            except Exception :
                ld.append(None)
            
        ld.append(annonce)

        for key, value in zip(self.data.keys(),ld):
            self.data[key].append(value)



    def scrap_annonces(self):
        for cat in self.category:
            for i in range(1,self.Np):
                link = f"{self.url}{cat}/uk/page{i}"
                self.driver.get(link)
                time.sleep(2)
                links_of_annonces = self.driver.find_elements(By.XPATH,config.xpaths['annonce'])
                self.lis.append( [a.get_attribute('href') for a in links_of_annonces])
        return list(itertools.chain.from_iterable(self.lis))



    def scrap(self):
        for annonce in self.scrap_annonces() :
            self.scrap_data(annonce)
        df = pd.DataFrame(self.data)
        output_dir = r'C:\Users\Youcode\ETL_project\data'
        os.makedirs(output_dir, exist_ok=True)
        df.to_csv(os.path.join(output_dir, 'extraction.csv'), encoding='utf-8', index=False)
        self.driver.quit()








chrome_options = Options()
chrome_options.add_argument("--headless")  
chrome_options.add_argument("--disable-gpu")  
chrome_options.add_argument("--disable-extensions")  
prefs = {"profile.managed_default_content_settings.images": 2}  
chrome_options.add_experimental_option("prefs", prefs)
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.implicitly_wait(30)

scrap_hpb = Scrap_hpb(driver,config.url,config.n_p,config.data,config.category)
