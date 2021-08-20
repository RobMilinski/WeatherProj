from django.shortcuts import render
import urllib.request
import json

class CityWeather:
    def __init__(self, name, lat, lon):
      self.name = name
      self.lat = lat
      self.lon = lon
      self.temp_min = 0
      self.temp_max = 0
      self.humidity = 0

canberra_details = CityWeather("Canberra", "-35", "149")
seattle_details = CityWeather("Seattle", "48", "-121")
london_details = CityWeather("London", "51", "0")

displayed_cities = (canberra_details, seattle_details, london_details)

def get_city_weather(mycity):
    lat = mycity.lat
    lon = mycity.lon

    app_key = '75523f4c2e67ef3ab67afe0d532a2795'
    URL = 'http://api.openweathermap.org/data/2.5/weather?'

    if mycity.name != '':
        URL += 'q=' + mycity.name + '&units=metric&appid=' + app_key
    else:
        URL += 'lat=' + lat + '&lon=' + lon + '&units=metric&appid=' + app_key

    source = urllib.request.urlopen(URL).read()

    raw_weather_data = json.loads(source)
    mycity.temp_min = str(raw_weather_data['main']['temp_min']) + ' °C'
    mycity.temp_max = str(raw_weather_data['main']['temp_max']) + ' °C'
    mycity.humidity = str(raw_weather_data['main']['humidity']) + ' %'

def get_displayed_cities_weather(cities_list):
    for city in cities_list:
        city_weather = get_city_weather(city)

def weatherapp(request):
    if request.method == "POST":
        input_city = CityWeather(request.POST['city'], request.POST['latitude'], request.POST['longitude'])
        get_city_weather(input_city)
    #else:
    #    print('hello world')
    #return render(request, 'weather/weatherapp.html', data)
    get_displayed_cities_weather(displayed_cities)
    return render(request, 'weather/weatherapp.html', {'displayed_cities': displayed_cities})