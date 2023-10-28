# web_driver_utils.py
'''
Selenium Web Driver configuration file
'''
import time
import pandas as pd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from custom_proxy import make_request

# proxy = make_request()

def initialize_chrome_webdriver(proxy):
    # Initialize and configure the Chrome WebDriver
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("window-size=1920,1080")
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--disable-gpu')
    # chrome_options.add_argument("--no-sandbox")
    # chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument(f'--proxy-server={proxy}')
    service = webdriver.chrome.service.Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

# Web driver for Firefox
def initialize_firefox_webdriver(): 
    # driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    service = webdriver.firefox.service.Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    return driver


# creating a DF once all malls have been extracted
def creating_DF(mall_names, mall_categories, Rates, ratings, Location_address):
    print('One second... creating our dataframe')
    time.sleep(2)

    data = pd.DataFrame({
                'Mall Name': mall_names,
                'Mall Category': mall_categories,
                'Star Rating': Rates,
                'Ratings': ratings,
                'Location': Location_address,
                # 'Service available': Services_Offered,
    })

    print('Here is your dataframe...')
    time.sleep(2)
    print(data)

    print('saving data to csv file...')
    time.sleep(2)
    data.to_csv('malls.csv', index=False, encoding='utf-8')
    print('CSV file is ready')