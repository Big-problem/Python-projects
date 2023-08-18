# Learn some basic about API
import requests

API_KEY = '500fc3ddeb4a9cd7363dd1786fc5ed1a'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

city = input('Enter a city name: ')
request_url = f'{BASE_URL}?appid={API_KEY}&q={city}'
response = requests.get(request_url)

if response.status_code == 200: # request success
    data = response.json() # turn the json data into python dictionary

    weather = data['weather'][0]['description']
    temperature = round(data['main']['temp'] - 273.15, 2) # kelvin to celsius
    
    print(f'Weather: {weather}')
    print(f'Temperature: {temperature} celsius')
else:
    print('An error occurred.')