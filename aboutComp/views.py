# howdy/views.py
from django.shortcuts import render
from django.views.generic import TemplateView

# Add this view
class AboutPageView(TemplateView):
    template_name = "aboutComp/about.html"