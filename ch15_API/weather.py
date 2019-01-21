

import requests

endpoint = "http://api.openweathermap.org/data/2.5/weather"
payload = {"q": "London,UK", "units":"metric", "appid":"open weather App API key"}
response = requests.get(endpoint, params = payload)
data = response.json()


print(data)
print('This is what data looks like: \n')
print(response.url)
print(response.status_code)
print(response.headers["content-type"])

    

















