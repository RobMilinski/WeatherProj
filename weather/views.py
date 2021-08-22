from django.shortcuts import render
import urllib.request
import json
from datetime import datetime

#CityWeather class created, each city/location has these attributes
class CityWeather:
    def __init__(self, name, lat, lon):
      self.name = name
      self.lat = lat
      self.lon = lon

#locations given by Uni assignment
loc1_details = CityWeather("Lake District National Park", "54.4609", "-3.0886")
loc2_details = CityWeather("Corfe Castle", "50.6395", "-2.0566")
loc3_details = CityWeather("The Cotswolds", "51.8330", "-1.8433")
loc4_details = CityWeather("Cambridge", "52.2053", "0.1218")
loc5_details = CityWeather("Bristol", "51.4545", "-2.5879")
loc6_details = CityWeather("Oxford", "51.7520", "-1.2577")
loc7_details = CityWeather("Norwich", "52.6309", "1.2974")
loc8_details = CityWeather("Stonehenge", "51.1789", "-1.8262")
loc9_details = CityWeather("Watergate Bay", "50.4429", "-5.0553")
loc10_details = CityWeather("Birmingham", "52.4862", "-1.8904")

#list of assigned cities, user assigned to be inserted later in position 0
displayed_cities = [loc1_details, loc2_details, loc3_details, loc4_details]#, loc5_details, loc6_details, loc7_details, loc8_details, loc9_details, loc10_details]

def get_city_weather(mycity):
    lat = mycity.lat
    lon = mycity.lon
    
    #https://openweathermap.org/api/one-call-api OneCall API information
    app_key = '75523f4c2e67ef3ab67afe0d532a2795'
    URL = 'http://api.openweathermap.org/data/2.5/onecall?'

    #if mycity.name != '':
    #    URL += 'q=' + mycity.name + '&units=metric&appid=' + app_key
    #else:
    URL += 'lat=' + lat + '&lon=' + lon + '&exclude=hourly,minutely,alerts&units=metric&appid=' + app_key

    #saves and converts weather data inso JSON file
    source = urllib.request.urlopen(URL).read()
    raw_weather_data = json.loads(source)

    #important weather information for each location
    mycity.main = str(raw_weather_data['current']['weather'][0]['main']),
    mycity.icon = "http://openweathermap.org/img/w/" + raw_weather_data['current']['weather'][0]['icon'] + ".png"
    mycity.description = str(raw_weather_data['current']['weather'][0]['description'])
    mycity.feels_like = str(raw_weather_data['current']['feels_like']) + ' °C'
    mycity.temp_min = str(raw_weather_data['daily'][0]['temp']['min']) + ' °C'
    mycity.temp_max = str(raw_weather_data['daily'][0]['temp']['max']) + ' °C'
    mycity.humidity = str(raw_weather_data['current']['humidity']) + ' %'
    mycity.pressure = str(raw_weather_data['current']['pressure']) + ' hPa'
    mycity.dew_point = str(raw_weather_data['current']['dew_point']) + ' °C'
    mycity.wind = str(raw_weather_data['current']['wind_speed']) + ' m/s'
    mycity.uv_index = str(raw_weather_data['daily'][0]['uvi'])
    mycity.sunrise = datetime.utcfromtimestamp(int(str(raw_weather_data['current']['sunrise']))).strftime('%H:%M:%S')
    mycity.sunset = datetime.utcfromtimestamp(int(str(raw_weather_data['current']['sunset']))).strftime('%H:%M:%S')

def get_displayed_cities_weather(cities_list):
    #for each location in list, run method
    for city in cities_list:
        city_weather = get_city_weather(city)

def weatherapp(request):
    if request.method == "POST":
        #add user defined location to cities list
        input_city = CityWeather(request.POST['city'], request.POST['latitude'], request.POST['longitude'])
        displayed_cities.insert(0, input_city)
    
    get_displayed_cities_weather(displayed_cities)
    return render(request, 'weather/weatherapp.html', {'displayed_cities': displayed_cities})