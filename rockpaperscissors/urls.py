from django import views
from django.urls import path
from . import views

app_name = "rps"
urlpatterns = [
    path('game/', views.gameView, name='game')
]