# Initialize the WebDriver (make sure you have chromedriver installed)
'''
Script to grab the names of Dubai malls
'''

import random
import os
import string
import openpyxl
from bs4 import BeautifulSoup as BSoup
import requests
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
from configured_selenium_driver import initialize_webdriver, creating_DF

driver = initialize_webdriver()

# Placeholders for our data frame
mall_names = []
mall_categories = []
All_malls = []
ratings = []
Rates = []
Location_address = []
Services_Offered = []

page_counter = 0

# Calculate the total number of records and pages
total_records = 48
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
        print('Page Counter file found')
        with open("page_counter.txt", "r") as file:
            saved_page_counter = int(file.read())
            if saved_page_counter >= 1:
                page_counter = saved_page_counter + 1

    # looping through all pages
    for page_number in range(1, total_pages + 1):    
        sleep_duration = random.uniform(2, 5)   # sleep randomly between each page   
        time.sleep(sleep_duration)   # Sleep for the random duration
        
        # Construct the page URL
        Next_page = f"{base_url}/page/{page_number}/{coordinates}"

        # navigating to pages
        driver.get(Next_page)

        # Scrape the soup from the page
        soup = BSoup(driver.page_source, 'lxml') 

        # shows the page number
        print('')
        print(f"Malls on page {page_number}:")

        # ==== START Of finding and extracting mall names=======
        mall_wrap = soup.find_all('div', {'class': '_1kf6gff'})
        # # mall_names.extend([mall.find('div', {'class': '_zjunba'}).text for mall in mall_wrap])
        malls_found = len(mall_wrap)
        print(f'Malls found are {malls_found}')
        for mall in mall_wrap:
            time.sleep(1)
            mall.find('div', {'class': '_zjunba'})
            mall_text = mall.span.text.strip()
            print(mall_text)
            mall_names.append(mall_text)
        # =====================END OF FINDING MALLS ==================================

        time.sleep(1)

        # ===== FINDING MALL CATEGORY ========
        mall_category = soup.findAll('span', attrs={'class': '_oqoid'})
        No_of_mall_catgories = len(mall_category)
        print(f'The are {No_of_mall_catgories} mall categories')
        for category in mall_category:
            category_text = category.text.strip()
            print(category_text)
            mall_categories.append(category_text)

        # ===== END OF FINDING MALL CATEGORY ========

        time.sleep(1)

        # # ======finding ratings===================
        ratings_wrap = soup.find_all('div', {'class':'_1emmab1'})
        No_of_Ratings = len(ratings_wrap)
        print(f'Found {No_of_Ratings} ratings')
        for rating in ratings_wrap:
            rating_text = rating.find('div', {'class': '_jspzdm'}).text.strip()
            rate_text = rating.find('div', {'class': '_y10azs'}).text.strip()
            
            time.sleep(1)

            print(rate_text)
            Rates.append(rate_text)

            print(rating_text)
            ratings.append(rating_text)
        # ========= end of ratings ======================

        # ====== LOCATION ==============================================
        locations = soup.find_all('span', attrs={'class':'_14quei'})
        No_of_locations = len(locations)
        print(f'There are {No_of_locations} locations available')
        for location in locations:
            time.sleep(1)
            location_text = location.text.strip()
             # Filter out non-printable characters
            location_text = ''.join(filter(lambda x: x in string.printable, location_text))
            print(location_text)
            # location_text = location_text.replace(' ', '')
            time.sleep(1)
            Location_address.append(location_text)
        # ====== end of location ======================================

        # ===== services offered ===============
        # services = soup.findAll('div', attrs={'class':'_d76pv4'})
        # No_of_services_found = len(services)
        # print(f'There are {No_of_services_found} services available')
        
        # for service in services:
        #   if service is not None:
        #     service_text = service.text
        #     print(service_text)
        #     time.sleep(1)
        #     Services_Offered.append(service_text if service_text else None)
        # # ===== end of services offered ================
        
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

# call the create DF function
creating_DF(mall_names, mall_categories, Rates, ratings, Location_address)
   
# Close the WebDriver when done
while True:
    command = input("Enter Crtl + C to quit")
    time.sleep(1)
