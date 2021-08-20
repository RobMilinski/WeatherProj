from django.shortcuts import render

# Add this view
def feedbackapp(request):
    return render(request, 'feedback/feedbackapp.html')