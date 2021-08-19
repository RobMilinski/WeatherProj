# howdy/urls.py
from django.conf.urls import url
from customerFeedback import views

urlpatterns = [
    url(r'^feedback/$', views.FeedbackPageView.as_view()), # Add this /about/ route
]