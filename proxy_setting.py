import requests

proxies = {
#    'http': 'http://50.170.90.25:80',
   'http': 'http://38.49.140.190:999'
}

url = 'https://httpbin.org/ip'
response = requests.get(url, proxies=proxies)

# print(f'Status Code: {response.status_code}')
print(response.json())
