import requests
from bs4 import BeautifulSoup as Bsoup
from configured_selenium_driver import initialize_chrome_webdriver, initialize_firefox_webdriver
from selenium.webdriver.common.by import By
from time import sleep
from pandas import DataFrame as df
import threading

# url = 'https://www.camplify.com.au/'
url = 'https://www.camplify.com.au/s?seed=14431&page=1'

# place holders for data frame
Name_of_RV_cards = []
Description_of_RV_cards = []
Types_of_RV_Cards = []
Location_of_RV_cards = []
Ratings_of_RV_cards = []
Prices_of_RV_cards = []

def get_cookies(url):
    try:
        resp = requests.get(url)
        cookies = resp.cookies

        print(f'cookies retireved:  {cookies}')
        cookes_retrieved = len(cookies)
        print(f'{cookes_retrieved} cookies retrieved')

        for number,cookie in enumerate(cookies, start=1):
            print(f'{number}: {cookie}')
    except Exception as error:
        print(f'error occured {error}')
        return None



# get_cookies(url) # funtion to get cookies

driver = initialize_chrome_webdriver()
driver.get(url)

# resp = driver.page_source

wait = driver.implicitly_wait(10) # wait for elements to appear

# navbar = driver.find_element(By.ID, "navbar-content")
# results_container = driver.find_element(By.ID, "results-container")
# h2_headers = driver.find_elements(By.TAG_NAME, "h2")
# SearchRvList__Result = driver.find_elements(By.CLASS_NAME, "SearchRvList__Result")


# Define a function for thread 1
def thread1(RV_Card):
    try:
        # Type of RV
        Rv_Card_Name = RV_Card.find_element(By.CSS_SELECTOR, "div.Text.RvCard__Title").text
        print(Rv_Card_Name)
        Name_of_RV_cards.append(Rv_Card_Name)
    except Exception as e:
        print(f"Thread 1 error: {e}")

# Define a function for thread 2
def thread2(RV_Card):
    try:
        # RV Description and Type of RV
        Rv_Card_Description = RV_Card.find_element(By.CLASS_NAME, "RvCard__Description").text
        Split_RV_description = Rv_Card_Description.split()[:2]
        RV_Description_joined = ' '.join(Split_RV_description)
        print(RV_Description_joined)
        Description_of_RV_cards.append(RV_Description_joined)
    except Exception as e:
        print(f"Thread 2 error: {e}")

# RV CARD wrapper and container
RvCard__Details = driver.find_elements(By.CLASS_NAME, "RvCard__Details")

No_of_RvCard_per_page = len(RvCard__Details)

print(f'{No_of_RvCard_per_page} RVs found on page')

# Your loop through RvCard__Details (assuming you have a WebDriver instance)
for RV_Card in RvCard__Details:
    # Create and start two threads
    thread1_instance = threading.Thread(target=thread1, args=(RV_Card,))
    thread2_instance = threading.Thread(target=thread2, args=(RV_Card,))
    
    thread1_instance.start()
    thread2_instance.start()
    
    # Wait for both threads to finish
    thread1_instance.join()
    thread2_instance.join()





        
       

# resp = requests.get(url)

# soup = Bsoup(resp, 'lxml')
# print(soup)

# div_wrapper = soup.find_all('div', attrs={'class': 'wrapper'})
# divs = soup.find_all('div')
# # # divs = soup.find_all('div', attrs={'id': 'navbar-container'})
# print(divs)

# motor home data frame
print('creating dataframe')
sleep(2)

# DF
motor_home_data = df({
    'Name of RV': Name_of_RV_cards,
    'Desciption of RV': Description_of_RV_cards,
   
})


print('Here is your dataframe...')
sleep(2)
print(motor_home_data)

print('saving data to csv file...')
sleep(2)
# motor_home_data.to_csv('motor_homes.csv', index=False, encoding='utf-8')
motor_home_data.to_csv('homes.csv', index=False)
print('CSV file is ready')