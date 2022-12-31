import requests
import json

api_key = 'YOUR_API_KEY'

# Set the address and other parameters for the request
address = '207 N. Defiance St, Archbold, OH'
params = {
    'address': address,
    'key': api_key,
}

# Make the request to the API
response = requests.get('https://maps.googleapis.com/maps/api/geocode/json', params=params)

# Check the status code of the response
if response.status_code == 200:
    # Load the response data into a Python object
    data = response.json()
    
    # Print the coordinates of the first result
    if len(data['results']) > 0:
        result = data['results'][0]
        print(result['geometry']['location'])
else:
    print('An error occurred:', response.status_code)