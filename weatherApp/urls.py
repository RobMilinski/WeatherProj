from django.urls import path
from . import views
from weatherApp import views
from django.conf.urls import url

urlpatterns = [
    path(r'^weather/$', views.weather),
    url(r'^weather/$', views.WeatherPageView.as_view()),
]