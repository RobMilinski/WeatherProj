from django.shortcuts import render

# Add this view
def aboutapp(request):
    return render(request, 'about/aboutapp.html')
    