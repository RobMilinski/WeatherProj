from django.shortcuts import render

# Add this view

def futureapp(request):
    return render(request, 'future/futureapp.html')
