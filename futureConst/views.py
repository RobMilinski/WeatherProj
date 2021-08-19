# howdy/views.py
from django.shortcuts import render
from django.views.generic import TemplateView

# Add this view
class FuturePageView(TemplateView):
    template_name = "futureConst/future.html"