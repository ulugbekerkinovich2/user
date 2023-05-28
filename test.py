import requests
import json

url = 'https://data.egov.uz/apiPartner/Partner/WebService'
params = {
    'token': '6456300b8e739cc5be9c6087',
    'name': '1-007-0017',
    'offset': 0,
    'limit': 5000,
    'lang': 'uz'
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    # Print the JSON data in a pretty format
    print(json.dumps(data, indent=4))
else:
    print('Error:', response.status_code)
