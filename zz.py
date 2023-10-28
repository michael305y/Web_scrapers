import time
from custom_proxy import make_request
from configured_selenium_driver import initialize_chrome_webdriver

# driver = initialize_chrome_webdriver()
working_proxies = make_request()
# url = "http://icanhazip.com"
URL = 'http://httpbin.org'  

# for page_number in range(1, 5):
#     # Choose a proxy from your list of working proxies
proxy = working_proxies[1]  # Adjust the index as needed

driver = initialize_chrome_webdriver(proxy)
driver.implicitly_wait(10)

    # Rest of your code for scraping the page with the selected proxy
driver.get(URL)
    


# proxy = make_request()
# print(proxy)

# Close the WebDriver when done
while True:
    command = input("Enter Crtl + C to quit")
    time.sleep(1)