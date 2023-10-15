# import requests

# def address_to_zip(address):
#     api_key = 'AIzaSyALz1DBN_XoF__NhGxbFYRHKq2MyDhGQ4Q'  # Replace with your own API key
#     base_url = 'https://maps.googleapis.com/maps/api/geocode/json'
#     params = {
#         'address': address,
#         'key': api_key,
#     }

#     response = requests.get(base_url, params=params)

#     if response.status_code == 200:
#         data = response.json()
#         if data.get('status') == 'OK':
#             results = data.get('results', [])
#             if results:
#                 zip_code = None
#                 for component in results[0].get('address_components', []):
#                     if 'postal_code' in component.get('types', []):
#                         zip_code = component.get('long_name')
#                         break
#                 return zip_code

#     return None

# # Example usage:
# # address = "555 7th St Santa Monica CA"
# address = "WHITEHOUSE STATION"
# zip_code = address_to_zip(address)

# if zip_code:
#     print("ZIP Code:", zip_code)
# else:
#     print("ZIP Code not found for the given address.")


import requests

def find_zip_code_with_bing(address):
  """Finds the ZIP code of a given address using Bing Maps.

  Args:
    address: The address to find the ZIP code for.

  Returns:
    The ZIP code of the given address, or None if the ZIP code cannot be found.
  """

  api_key = 'YOUR_API_KEY'
  base_url = 'https://dev.virtualearth.net/REST/V1/Locations'
  params = {
    'key': api_key,
    'q': address,
  }

  response = requests.get(base_url, params=params)

  if response.status_code == 200:
    data = response.json()
    if data.get('status') == 'OK':
      results = data.get('results', [])
      if results:
        zip_code = None
        for address_component in results[0].get('addressComponents', []):
          if address_component.get('postalCode'):
            zip_code = address_component.get('postalCode')
            break
        return zip_code

  return None

# Example usage:
# address = "101 MARGARAT CT"
address = "MATAWAN NJ"
# address = "WHITEHOUSE STATION, NJ"
zip_code = find_zip_code_with_bing(address)

if zip_code:
  print("ZIP Code:", zip_code)
else:
  print("ZIP Code not found for the given address.")
