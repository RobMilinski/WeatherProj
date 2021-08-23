import urllib.request
import json
from datetime import datetime

#CityWeather class created, each city/location has these attributes
class CityWeather:
    def __init__(self, name, lat, lon):
        self.name = name
        self.lat = lat
        self.lon = lon

    def get_city_weather(self):
        lat = self.lat
        lon = self.lon
        
        #https://openweathermap.org/api/one-call-api OneCall API information
        app_key = '75523f4c2e67ef3ab67afe0d532a2795'
        URL = 'http://api.openweathermap.org/data/2.5/onecall?'
        URL += 'lat=' + lat + '&lon=' + lon + '&exclude=hourly,minutely,alerts&units=metric&appid=' + app_key

        #saves and converts weather data inso JSON file
        source = urllib.request.urlopen(URL).read()
        raw_weather_data = json.loads(source)

        #important weather information for each location
        self.main = str(raw_weather_data['current']['weather'][0]['main']),
        self.icon = "http://openweathermap.org/img/w/" + raw_weather_data['current']['weather'][0]['icon'] + ".png"
        self.description = str(raw_weather_data['current']['weather'][0]['description'])
        self.feels_like = str(raw_weather_data['current']['feels_like']) + ' °C'
        self.temp_min = str(raw_weather_data['daily'][0]['temp']['min']) + ' °C'
        self.temp_max = str(raw_weather_data['daily'][0]['temp']['max']) + ' °C'
        self.humidity = str(raw_weather_data['current']['humidity']) + ' %'
        self.pressure = str(raw_weather_data['current']['pressure']) + ' hPa'
        self.dew_point = str(raw_weather_data['current']['dew_point']) + ' °C'
        self.wind = str(raw_weather_data['current']['wind_speed']) + ' m/s'
        self.uv_index = str(raw_weather_data['daily'][0]['uvi'])
        self.sunrise = datetime.utcfromtimestamp(
            int(str(raw_weather_data['current']['sunrise'])) 
            #convert UTC to local time
            + int(str(raw_weather_data['timezone_offset']))).strftime('%H:%M:%S')
        self.sunset = datetime.utcfromtimestamp(
            int(str(raw_weather_data['current']['sunset']))
            #convert UTC to local time
            + int(str(raw_weather_data['timezone_offset']))).strftime('%H:%M:%S')