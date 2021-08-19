# howdy/urls.py
from django.conf.urls import url
from futureConst import views

urlpatterns = [
    url(r'^future/$', views.FuturePageView.as_view()), # Add this /about/ route
]