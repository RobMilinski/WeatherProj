from django.shortcuts import render
import urllib.request
import json

city_details = ['Canberra', 'Sydney']

canberra_details = {"name": "Canberra", "latitude": "-35", "longitude": "149"}
sydney_details = {"name": "Sydney", "latitude": "-34", "longitude": "151"}

def weatherapp(request):
        if request.method == "POST":
            app_key = '75523f4c2e67ef3ab67afe0d532a2795'

            URL = 'http://api.openweathermap.org/data/2.5/weather?'

            city = request.POST['city']
            latitude = request.POST['latitude']
            longitude = request.POST['longitude']

            if city != '':
                URL += 'q=' + city + '&units=metric&appid=' + app_key
            else:
                URL += 'lat=' + latitude + '&lon=' + longitude + '&units=metric&appid=' + app_key
            
            source = urllib.request.urlopen(URL).read()

            raw_weather_data = json.loads(source)

            data = {
                "name": str(raw_weather_data['name']),
                "temp_min": str(raw_weather_data['main']['temp_min']) + ' °C',
                "temp_max": str(raw_weather_data['main']['temp_max']) + ' °C',
                "humidity": str(raw_weather_data['main']['humidity']) + ' %',
            }
            print(data)
        else:
            data = {}

        return render(request, 'weather/weatherapp.html', data)
