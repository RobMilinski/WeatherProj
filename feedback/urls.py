from django.conf.urls import url
from . import views

from django.contrib import admin
from .views import feedbackapp

urlpatterns = [
    url(r'^$', views.feedbackapp),
]