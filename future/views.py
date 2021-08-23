from django.shortcuts import render

# Add this view

def futureapp(request):
    #display future app template
    return render(request, 'future/futureapp.html')
