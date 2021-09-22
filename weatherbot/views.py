from django.shortcuts import render
from django.http import HttpResponse
import urllib.request
import json
from .weatherbot_logic import GetTrainedBotResponse
from .weather_bot import GetWeatherBotAnswer

# Add this view
def weatherbotapp(request):
    if request.method != "POST":
        chat_history = ""
        request.session.clear()
        return render(request, 'weatherbot/weatherbotapp.html', {})

    if request.method == 'POST':
        question = request.POST['question']

        chat_history = request.session.get('chat_history')
        if(chat_history == None):
            chat_history = ""

        if(chat_history):
            chat_history = '\r\n\r\n' + chat_history

        # user name requested only on first get call
        user_name = request.session.get('user_name')
        if(user_name == None):
            user_name = request.POST['user_name']
        
        request.session['user_name'] = user_name

        answer = GetWeatherBotAnswer(question)

        if answer == "":
            answer = GetTrainedBotResponse(question)

        request.session['chat_history'] =  user_name + ': ' + question + '\r\nChatbot: ' + answer + chat_history
        
        return render(request, 'weatherbot/weatherbotapp.html', 
                {'question': question, 'answer': answer, 'user_name': user_name, 'chat_history': chat_history}
                )

    else:
        return render(request, 'weatherbot/weatherbotapp.html')
