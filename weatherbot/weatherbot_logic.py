from django.http import HttpResponse
from django.shortcuts import render

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import json

my_bot = ChatBot('WeatherBot',
                    logic_adapters=['chatterbot.logic.MathematicalEvaluation',
                                    'chatterbot.logic.BestMatch'], 
                    # storage_adapter=['chatterbot.storage.SQLStorageAdapter']
                                 )
def trainBotWithList(bot):
    small_talk = ['hi there!',
                'hi!',
                'how do you do?',
                'how are you?',
                'i\'m cool.',
                'fine, you?',
                'always cool.',
                'i\'m ok',
                'glad to hear that.',
                'i\'m fine',
                'glad to hear that.',
                'i feel awesome',
                'excellent, glad to hear that.',
                'not so good',
                'sorry to hear that.',
                'what\'s your name?',
                'i\'m pybot. ask me a \n math question, please.']
    math_talk_1 = ['pythagorean theorem',
                'a squared plus b squared equals c squared.']
    math_talk_2 = ['law of cosines',
                'c**2 = a**2 + b**2 - 2 * a * b * cos(gamma)']

    list_trainer = ListTrainer(my_bot)

    for item in (small_talk, math_talk_1, math_talk_2):
        list_trainer.train(item)

def trainBotWithCorpus(bot):
    corpus_trainer = ChatterBotCorpusTrainer(bot)
    corpus_trainer.train('chatterbot.corpus.english')

def trainBotWithCustom(bot):
    with open('nfl6.json', 'r') as jfile:
        qa_data= jfile.read()

    qa_json = json.loads(qa_data)
    train = []

    for k, r in enumerate(qa_json):
        train.append(r['question'])
        train.append(r['answer'])
    trainer = ListTrainer(bot)
    trainer.train(train)

# trainBotWithCustom(my_bot)
trainBotWithList(my_bot)
# trainBotWithCorpus(my_bot)

def get_bot_response(question):
    return my_bot.get_response(question).text
