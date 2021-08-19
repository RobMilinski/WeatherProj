# howdy/views.py
from django.shortcuts import render
from django.views.generic import TemplateView

# Add this view
class FeedbackPageView(TemplateView):
    template_name = "customerFeedback/feedback.html"