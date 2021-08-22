from django.shortcuts import render
import urllib.request
import json
from datetime import datetime
from .city_weather import CityWeather

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



def get_displayed_cities_weather(cities_list):
    #for each location in list, run method
    for city in cities_list:
        city.get_city_weather()

def weatherapp(request):
    #list of assigned cities, user assigned to be inserted later in position 0
    #displayed_cities = [loc1_details, loc2_details]
    displayed_cities = [loc1_details, loc2_details, loc3_details, loc4_details, loc5_details, loc6_details, loc7_details, loc8_details, loc9_details, loc10_details]
    
    if request.method == "POST":
        #add user defined location to cities list
        select_box_json = request.POST['cityselectbox']
        select_city = None
        if select_box_json != '':
            select_city = json.loads(select_box_json)

        if request.POST['latitude'] != '' and request.POST['longitude'] != '':
            input_city = CityWeather(request.POST['city'], request.POST['latitude'], request.POST['longitude'])
            displayed_cities.insert(0, input_city)
        elif select_city != None:
            input_city = CityWeather(select_city['city'], select_city['lat'], select_city['lon'])
            displayed_cities.insert(0, input_city)

    get_displayed_cities_weather(displayed_cities)
    return render(request, 'weather/weatherapp.html', {'displayed_cities': displayed_cities})
    