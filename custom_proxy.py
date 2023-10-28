from pprint import pprint
import random
import requests
import pandas as pd
from bs4 import BeautifulSoup as bs


USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
# US english
LANGUAGE = "en-US,en;q=0.5"

# function to get proxies
def get_free_proxies():
    url = "https://free-proxy-list.net/"
    # get the HTTP response and construct soup object
    response = requests.get(url)

    soup = bs(response.content, "html.parser")

    proxies = []
    # table = soup.find('div', attrs={'class':'table-responsive'})
    table = soup.find('tbody')
    # print(table)
    table_rows = table.find_all('tr')
    for row in table_rows:
        # print(row.text)   # prints all the rows
        try:
            ip_address = row.find_all('td')[0].text
            port = row.find_all('td')[1].text
            host = f'{ip_address}:{port}'
            # print(host)
            proxies.append(host)
            # print(proxies)
        except IndexError:
            continue
    return proxies

# function to create session
def get_session():
    proxies = get_free_proxies()
    session = requests.Session()

    proxy = random.choice(proxies)
    print(f'current proxy being used {proxy}')
    
    session.proxies = {'http': proxy, 'https': proxy}

    return session

# getting the real IP
def current_IP():
    # real_ip = requests.Session()
    # my_ip = real_ip.get("http://icanhazip.com").text
    my_ip = requests.get("http://icanhazip.com").text
    print(f'your real ip is: {my_ip}')

# proxy_a = get_free_proxies()
# print(proxy_a[-1])

#funtion to get the proxy ip
# def get_proxy_ip():
#     try:
#         proxy_ip = get_session()
#         my_proxy_ip = proxy_ip.get("http://icanhazip.com", timeout=2)
        
#         if my_proxy_ip.status_code == 200:
#             print(my_proxy_ip.text.strip())
#         #     return
#     except requests.exceptions.RequestException as error:
#         print(error)
#         return get_proxy_ip

# get_proxy_ip()

def make_request():
    url = 'http://icanhazip.com'
    # url = 'https://y.qq.com/n/ryqq/songDetail/003VQTd042uLqQ'
    working_proxies = []
    # ANSI escape codes for text colors
    GREEN = '\033[92m'  # Green color
    RESET = '\033[0m'    # Reset to default color

    List_of_Proxies = get_free_proxies()   # gets all proxies

    print(f'{len(List_of_Proxies)} proxies found')
    number_of_proxies_to_use = List_of_Proxies[:10]
    print(f'Now using {len(number_of_proxies_to_use)} proxies')
    for number,proxy in enumerate(number_of_proxies_to_use, start=1):
        # print(proxy)
        # split the proxy string then convert into a dictionary
        ip_addrress, port = proxy.split(':')
        # print(ip_addrress)
        # print(port)
        proxy_dict = {
            # 'http': f'http://{ip_addrress}:{port}',  # method 1
            # 'https': f'https://{ip_addrress}:{port}'
            'http': proxy,   # method 2
            'https': proxy
            }
        print(number, proxy_dict)

        try:
            # response = requests.Session() # when you want to use sessions to make request to target
            response = requests.get(url, proxies=proxy_dict, timeout=2)  # when you make a one off request wiithout maintaining session
            if response.status_code == 200:
                print(f'{GREEN}working: with status code {response.status_code} {RESET}')
                my_ip = response.text
                print(f'your current ip is: {my_ip}')
                working_proxies.append(proxy_dict)
            else:
                print(f'{RESET}request failed with status code {response.status_code}')
                # continue
        except TimeoutError as error:
            print(f'{RESET}Timeout {error} for proxy: {proxy_dict}')
            continue
        except ConnectionError as error:
            print(f'{RESET}Connection error {error} for proxy: {proxy_dict}')
            continue
        except requests.exceptions.RequestException as error:
            print(f'{RESET} error: {error} for proxy: {proxy_dict}')
            continue
        print(working_proxies)
    return working_proxies

if __name__ == '__main__':
    proxies = make_request()
    pprint(proxies)


