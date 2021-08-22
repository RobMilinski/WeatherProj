from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ContactForm

# Add this view
#def feedbackapp(request):
#    return render(request, 'feedback/feedbackapp.html')

def feedbackapp(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        customername = request.POST['customername']
        customername = request.POST['customeremail']
        customername = request.POST['customercomment']
    else:
        form = ContactForm()
    
    return render(request, 'feedback/feedbackapp.html', {'form': form})