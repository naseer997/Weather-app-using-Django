from django.shortcuts import render
from django.contrib import messages
import requests
import datetime


def home(request):

    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'indore'

    WEATHER_API_KEY = "05c10248e3e6d47e35b0178979f3e042"

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}'

    PARAMS = {'units': 'metric'}

    image_url =  "https://images.pexels.com/photos/1118873/pexels-photo-1118873.jpeg"

    try:

        data = requests.get(url, params=PARAMS).json()

        print(data)   

        description = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        temp = data['main']['temp']
        day = datetime.date.today()

        return render(request, 'weatherapp/index.html', {
            'description': description,
            'icon': icon,
            'temp': temp,
            'day': day,
            'city': city,
            'exception_occurred': False,
            'image_url': image_url
        })

    except KeyError:

        print(data)   # optional debug here too

        exception_occurred = True
        messages.error(request, 'Entered data is not available to API')
        day = datetime.date.today()

        return render(request, 'weatherapp/index.html', {
            'description': 'clear sky',
            'icon': '01d',
            'temp': 25,
            'day': day,
            'city': 'indore',
            'exception_occurred': exception_occurred,
            'image_url': image_url
        })