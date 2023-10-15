import requests
from bs4 import BeautifulSoup as Bsoup
from configured_selenium_driver import initialize_chrome_webdriver, initialize_firefox_webdriver
from selenium.webdriver.common.by import By
from time import sleep
from pandas import DataFrame as df

driver = initialize_chrome_webdriver()

url_list = [
    'https://y.qq.com/n/ryqq/songDetail/0000MmOl2BQve2',
    'https://y.qq.com/n/ryqq/songDetail/002NLR4K2Gt2gn',
    'https://y.qq.com/n/ryqq/songDetail/0024lcFI0LP3c8',
    'https://y.qq.com/n/ryqq/songDetail/002Sv8SW4bNM83',
    'https://y.qq.com/n/ryqq/songDetail/002o0nAE0zrmZ7',
    'https://y.qq.com/n/ryqq/songDetail/0046GYHA2BjkfW',
    'https://y.qq.com/n/ryqq/songDetail/002wllz31cXL7b',
    'https://y.qq.com/n/ryqq/songDetail/002sI1ZF00DvPs',
    'https://y.qq.com/n/ryqq/songDetail/002m20Gy1CiguL',
    'https://y.qq.com/n/ryqq/songDetail/003VQTd042uLqQ'
]

# url = 'https://y.qq.com/n/ryqq/songDetail/003VQTd042uLqQ'
# url = 'https://y.qq.com/n/ryqq/songDetail/0000MmOl2BQve2'

# place holders for data frame
Album_Names = []
Release_Dates = []
comment_counts = []


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


# functiont to grab each album details
def get_details():
    get_cookies(url)

    # Default values incase elements are not found
    album_name = 'missing'
    release_date = 'missing'
    comment_count = 'missing'

    try:
        album_name = driver.find_element(By.CLASS_NAME, 'data__name_txt').text
    except Exception as error:
        print(f'Error getting album name: {error}')
    Album_Names.append(album_name)

    try:
        ul_data_info = driver.find_element(By.CSS_SELECTOR, 'ul.data__info')
        release_date = ul_data_info.find_elements(By.CSS_SELECTOR, 'li.data_info__item_song')[4].text
        print(release_date)
    except Exception as error:
        print(f'Error getting release date: {error}')
    Release_Dates.append(release_date)

    try:
        comment_count = driver.find_elements(By.CSS_SELECTOR, 'span.btn__txt')[3].text
    except Exception as error:
        print(f'Error getting comment count: {error}')
    comment_counts.append(comment_count)

    ## method 2 of appending element text to the defined lists
    # Album_Names.append(album_name)
    # Release_Dates.append(release_date)
    # comment_counts.append(comment_count)

# ...

# Create DataFrame
album_data = df({
    'Name of Album': Album_Names,
    'Date of Release': Release_Dates,
    'Number of comments': comment_counts,
})

# ...

print(album_data)


for url in url_list:
    driver.get(url)

    get_details()


# motor home data frame
print('creating dataframe')
sleep(2)

# DF
album_data = df({
    'Name of Album': Album_Names,
    'Date of Release': Release_Dates,
    'Number of comments': comment_counts,
})


print('Here is your dataframe...')
sleep(2)
print(album_data)

print('saving data to csv file...')
sleep(2)
# motor_home_data.to_csv('motor_homes.csv', index=False, encoding='utf-8')
album_data.to_csv('album_names.csv', index=False, encoding='utf-8')
print('CSV file is ready')
