from django.shortcuts import render
import requests
from decouple import config

def weather_view(request):
    weather_data = None
    error = None

    if 'city' in request.GET:
        city = request.GET['city']
        api_key = config('WEATHER_API_KEY')
        url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"

        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather_data = {
                'city': data['location']['name'],
                'temperature': data['current']['temp_f'],
                'description': data['current']['condition']['text'],
                'humidity': data['current']['humidity'],
                'wind_speed': data['current']['wind_kph'],
            }
        else:
            error = "City not found or API error."

    return render(request, 'weather/index.html', {
        'weather_data': weather_data,
        'error': error
    })
