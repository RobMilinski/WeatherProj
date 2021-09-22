from django.shortcuts import render
from django.http import HttpResponse
import urllib.request
import json
from .weatherbot_logic import get_bot_response
from .weather_bot import GetWeatherBotAnswer

# Add this view
def weatherbotapp(request):
    if request.method == 'POST':
        question = request.POST['question']
        
        name = 'Fred'
        answer = GetWeatherBotAnswer(question)

        if answer == "":
            answer = get_bot_response(question)

        return render(request, 'weatherbot/weatherbotapp.html', 
                {'question': question, 'answer': answer, 'name': name}
                )

    else:
        return render(request, 'weatherbot/weatherbotapp.html')
