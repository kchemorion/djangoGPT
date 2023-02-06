# myapp/views.py
from django.shortcuts import render
from chatterbot import ChatBot
#from chatterbot.ext.django_chatterbot import views as chatterbot_views
from django.views.decorators.csrf import csrf_exempt
#from chatterbot.ext.django_chatterbot import DjangoChatBot
import chatterbot
from . import chatgpt_adapter
# def chat_view(request):
#     return render(request, 'templates/chat.html')

def chat_view(request):
    # chatbot = ChatBot(
    #     'ChatGPT',
    #     read_only=True,
    #     logic_adapters=[
    #         {
    #             'import_path': 'chatterbot.logic.BestMatch'
    #         },
    #         {
    #             'import_path': 'chatgpt_adapter.ChatGPTAdapter',
    #             'model_name': 'chatgpt'
    #         }
    #     ]
    # )
    return render(request, 'templates/chat.html')



@csrf_exempt
def chat(request):
    return render(request, 'chat.html', {'chatbot': DJANGO_CHATBOT})
