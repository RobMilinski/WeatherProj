from django.shortcuts import render
import urllib.request
import json
from django.views.generic import TemplateView

#Create your views here.

class WeatherPageView(TemplateView):
    template_name = "weatherApp/weather.html"

def weather(request):
        if request.method == "POST":
            app_key = '75523f4c2e67ef3ab67afe0d532a2795'

            #city = request.POST['city']
            latitude = request.POST['latitude']
            longitude = request.POST['longitude']

            URL = 'http://api.openweathermap.org/data/2.5/weather?lat=' + latitude + '&lon=' + longitude + '&appid=' + app_key

            source = urllib.request.urlopen(URL).read()

            raw_weather_data = json.loads(source)

            data = {
                "temp_min": str(raw_weather_data['main']['temp_min']) + ' °C',
                "temp_max": str(raw_weather_data['main']['temp_max']) + ' °C',
                "humidity": str(raw_weather_data['main']['humidity']) + ' %',
            }
            print(data)
        else:
            data = {}

        return render(request, 'weather.html', data)