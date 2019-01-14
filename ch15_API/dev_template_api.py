import requests

# The base url to access the API information
endpoint_weather = "https://api.openweathermap.org/data/2.5/weather"
endpoint_postcode = "https://api.postcodes.io/postcodes/"

# The parameters to what exactly you need from the API
# The structure of this varies from API to API
payload = {"q": "Zermatt, CH", "units": "metric", "appid": "my app id in quotes"}

# Sometimes you don't need a parameter, just a value
postcode = "LE111LG"

# Before requesting anything from an API test the url by going to it in a browser
test_weather_url = (endpoint_weather, payload)
print(test_weather_url)

test_postcode_url = (endpoint_postcode + postcode)
print(test_postcode_url)

# If you get a decent response in a browser, you can go ahead and request it with Python
weather_response = requests.get(endpoint_weather, params=payload)
postcode_response = requests.get(endpoint_postcode + postcode)

# Convert your return into json
data_weather = weather_response.json()
data_postcode = postcode_response.json()

# To be able to read the data you need to look at what you actually get.
# Look at the type of brackets that surrounds each item in your json file.
# If it's {} it will work like a dictionary
# If it's [] it will work like a list
print(data_weather['weather'][0]['description'])
print(data_postcode['result']['longitude'])