from django.shortcuts import render, HttpResponse
import requests
from bs4 import BeautifulSoup as bs
import json

def get_weather_data(city):
    city = city.replace(' ','+')
    url = f'https://www.google.com/search?q=weather+of+{city}'
    USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.9"
    session = requests.Session()
    session.headers['user-agent'] = USER_AGENT
    session.headers['accept-language'] = LANGUAGE
    response = session.get(url)
    soup = bs(response.text, 'html.parser')
    # Extract Data and Add to Dictionary
    results = {}
    results['region'] = soup.find('span', attrs={'class':'BBwThe'}).text
    results['daytime'] = soup.find('div', attrs={'id':'wob_dts'}).text
    results['weather'] = soup.find('span', attrs={'id':'wob_dc'}).text
    results['temp'] = soup.find('span', attrs={'id':'wob_tm'}).text
    # print(results)
    return results

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



# Create your views here.
def home_view(request):
    # return render(request, 'home.html')
    # return HttpResponse('<h1>First Django Project</h1>')
    template_name = 'weather/home.html'

    if request.method == "GET" and 'city' in request.GET:
        city = request.GET.get('city')
        result = get_weather_data(city)
        context = {'result': result}
        print(context)
    else:
        context = {}
    return render(request, template_name, context)

def api_view(request):
    if request.method == "POST" and 'city' in request.POST:
        city = request.POST.get('city')
        result = weather_api(city)
        context = {'result': result}
    else:
        context = {}

    return render(request, 'weather/api.html', context)
