# howdy/urls.py
from django.conf.urls import url
from aboutComp import views

urlpatterns = [
    url(r'^about/$', views.AboutPageView.as_view()), # Add this /about/ route
]