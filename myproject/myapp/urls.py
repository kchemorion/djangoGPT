# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('chat/', views.chat_view, name='chat'),
  #  path('chatterbot/', views.chatterbot, name='chat'),
]
