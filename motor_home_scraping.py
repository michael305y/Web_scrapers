import requests
from bs4 import BeautifulSoup as Bsoup
from configured_selenium_driver import initialize_chrome_webdriver, initialize_firefox_webdriver
from selenium.webdriver.common.by import By
from time import sleep
from pandas import DataFrame as df

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

# RV CARD wrapper and container
RvCard__Details = driver.find_elements(By.CLASS_NAME, "RvCard__Details")

No_of_RvCard_per_page = len(RvCard__Details)

print(f'{No_of_RvCard_per_page} RVs found on page')

for RV_Card in RvCard__Details:
    try:
        sleep(1)

  # using threads for each operation and maybe each thread with a different IP
    # thread 1 
        # Type of RV
        Rv_Card_Name = RV_Card.find_element(By.CSS_SELECTOR, "div.Text.RvCard__Title").text
        print(Rv_Card_Name)
        Name_of_RV_cards.append(Rv_Card_Name)

    # thread 2
        # RV Description and Type of RV
        Rv_Card_Description = RV_Card.find_element(By.CLASS_NAME, "RvCard__Description").text
        # splits the description and gets the first 2 items back and joins them
        Split_RV_description =  Rv_Card_Description.split()[:2] 
        RV_Description_joined = ' '.join(Split_RV_description)
        print(RV_Description_joined)
        Description_of_RV_cards.append(RV_Description_joined)

        # Type of RV but its similar to the RV description so leave it
        Rv_Card_Type = RV_Card.find_element(By.CSS_SELECTOR, "div.Text.RvCard__Type").text
        print(Rv_Card_Type)
        Types_of_RV_Cards.append(Rv_Card_Type)
        
        Location_of_Rv = RV_Card.find_element(By.CSS_SELECTOR, "div.RvCard__LocationText").text #location of RV
        sleep(1)
        print(Location_of_Rv)
        Location_of_RV_cards.append(Location_of_Rv)

        # reviews
        Rv_card_review = RV_Card.find_element(By.CSS_SELECTOR, "div.Text.StarRatingWithCount__TotalReviews").text
        print(Rv_card_review)
        Ratings_of_RV_cards.append(Rv_card_review)
        
        # finding price
        Rv_card_price = RV_Card.find_element(By.CSS_SELECTOR, "div.RvCard__PriceValue").text
        print(Rv_card_price)
        Prices_of_RV_cards.append(Rv_card_price)
 
        
    except Exception as error:
        print(f'Error: {error}')


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
    'Type of RV': Types_of_RV_Cards,
    'Location of RV': Location_of_RV_cards,
    'Ratings Reviews of RV': Ratings_of_RV_cards,
    'Price of RV': Prices_of_RV_cards,
})


print('Here is your dataframe...')
sleep(2)
print(motor_home_data)

print('saving data to csv file...')
sleep(2)
# motor_home_data.to_csv('motor_homes.csv', index=False, encoding='utf-8')
motor_home_data.to_csv('motor_homes.csv', index=False)
print('CSV file is ready')