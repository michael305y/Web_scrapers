# Initialize the WebDriver (make sure you have chromedriver installed)
'''
Script to grab the names of Dubai malls
'''

import random
import os
import openpyxl
from bs4 import BeautifulSoup as BSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time
import pandas as pd

# Configurations of Edge WebDriver in headless mode
# Configure Chrome WebDriver in headless mode
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("window-size=1920,1080")
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')  # Disable GPU acceleration in headless mode
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
service = webdriver.chrome.service.Service(ChromeDriverManager().install())
# Pass in the Service object and Chrome options to the webdriver.Chrome method
# driver = webdriver.Chrome(service=service, options=chrome_options)
driver = webdriver.Chrome(service=service)

# Placeholders for our data frame
mall_names = []
All_malls = []
ratings = []
Rates = []
page_counter = 0

# Calculate the total number of records and pages
total_records = 12
records_per_page = 12
total_pages = total_records // records_per_page

# Base URL and coordinates
base_url = "https://2gis.ae/dubai/search/Malls"
coordinates = "55.199034%2C25.118495%2F11"

# getting started
print('connection is secure, lets start scraping')

try:
    # Check if there is a saved page counter
    if os.path.exists('page_counter.txt'):
        time.sleep(2)
        print('file found')
        with open("page_counter.txt", "r") as file:
            saved_page_counter = int(file.read())
            if saved_page_counter >= 1:
                page_counter = saved_page_counter + 1

    # looping through all pages
    for page_number in range(1, total_pages + 1):
        # sleep randomly between each page
        sleep_duration = random.uniform(2, 5)
        # Sleep for the random duration
        time.sleep(sleep_duration)
        
        # Construct the page URL
        Next_page = f"{base_url}/page/{page_number}/{coordinates}"
        # Next_page = f'https://2gis.ae/dubai/search/Malls/page/{page_number}?m=55.199034%2C25.118495%2F11'
        
        # navigating to pages
        driver.get(Next_page)

        # Scrape the content from the page
        content = BSoup(driver.page_source, 'lxml')

        # # malls found on each page
        # print('')
        # print(f"Malls on page {page_number}:")

        # ==== START Of finding and extracting mall names=======
        mall_wrap = content.find_all('div', {'class': '_1kf6gff'})
        # # mall_names.extend([mall.find('div', {'class': '_zjunba'}).text for mall in mall_wrap])
        
        for mall in mall_wrap:
            time.sleep(1)
            mall.find('div', {'class': '_zjunba'})
            # print(mall.span.text)
            mall_text = mall.span.text
            print(mall_text)
            mall_names.append(mall_text)
        # =====================END OF FINDING MALLS ==================================

        # ======finding ratings===================
        ratings_wrap = content.find_all('div', {'_1emmab1'})
        for rating in ratings_wrap:
            rating_text = rating.find('div', {'class': '_jspzdm'}).text
            rate_text = rating.find('div', {'class': '_y10azs'}).text
            time.sleep(1)

            print(rate_text)
            Rates.append(rate_text)

            print(rating_text)
            ratings.append(rating_text)
        # ========= end of ratings ======================
   
        # counting number of pages that have been scrapped
        page_counter += 1

        # slleps after every 5 pages have been scraped
        if page_counter % 2 == 0:
            print('Taking a breather LOL... be back in a few MINUTES')
            # time.sleep(5)
            time.sleep(sleep_duration)
            with open("page_counter.txt", "w") as file:
                file.write(str(page_number))
       
           
                
except Exception as e:
    print(f"An exception occurred: {e}")

# creating a DF once all malls have been extracted
print('One second... creating our dataframe')
time.sleep(2)

data = pd.DataFrame({
            'Mall Name': mall_names,
            'Rates': Rates,
            'Ratings': ratings,
})

print('Here is your dataframe...')
time.sleep(2)
print(data)

# # print('saving data to a csv file...')
# data.to_csv('test2.csv', index=False)
   
# Close the WebDriver when done
while True:
    command = input("Enter Crtl + C to quit")
    time.sleep(1)
