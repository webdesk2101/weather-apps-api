import requests
import json

def weather_api(city):
    api_key = '78e9acc9499f954807ced63fa94dbe5f'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)
    data = json.loads(response.text)
    result = {}
    result['lon'] = data['coord']['lon']
    result['lat'] = data['coord']['lat']
    result['name'] = data['name']
    result['temp'] = data['main']['temp']
    result['humidity'] = data['main']['humidity']
    return result

# print(weather_api('London'))

