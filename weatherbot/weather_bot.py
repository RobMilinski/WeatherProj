import urllib.request
import json

# expects city name and returns weather json
def GetCityWeather(city):
    
    app_key = '75523f4c2e67ef3ab67afe0d532a2795'
    url = 'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=' + app_key

    source = urllib.request.urlopen(url).read()
    raw_weather_data = json.loads(source)

    answer = 'In ' + city + ' it is ' + str(raw_weather_data['weather'][0]['description']) + ' and the temperature is ' + str(raw_weather_data['main']['temp']) + ' °C'

    return answer

# expects a question text and returns answer
# if question contains 'weather' or 'temperature' and one of the predefined cities, it returns answer text containing weather info
# question example: "what is the weather in Sydney?" or "temperature in canberra"
# e.g. "It is raining and the temperature is 23 degrees."
def GetWeatherBotAnswer(question):
    question = question.replace("?","")
    question = question.lower()
    words = question.split()

    main_cities = ['sydney', 'canberra', 'london', 'madrid']

    question_contains_city = False
    user_city = ''
    for word in words:
        if word in main_cities :
            user_city = word
            question_contains_city = True

    question_contains_temperature = 'temperature' in words
    question_contains_weather = 'weather' in words

    do_get_weather_data = (question_contains_temperature or question_contains_weather) and question_contains_city
    if do_get_weather_data:
        return GetCityWeather(user_city)
    else:
        return ''

# for testing purposes, see below

# question = 'temperature in sydney'
# answer = GetWeatherBotAnswer(question)
# print(question, answer)

# question = 'weather in madrid'
# answer = GetWeatherBotAnswer(question)
# print(question, answer)

# question = 'temperature in rome'
# answer = GetWeatherBotAnswer(question)
# print(question, answer)

# question = 'how are you'
# answer = GetWeatherBotAnswer(question)
# print(question, answer)