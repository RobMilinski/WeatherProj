from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ContactForm

# Add this view
#def feedbackapp(request):
#    return render(request, 'feedback/feedbackapp.html')

def feedbackapp(request):
    if request.method == 'GET':
        return render(request, 'feedback/feedbackget.html')
    else:
        name = request.POST['customername']
        email = request.POST['customeremail']
        feedback = request.POST['customerfeedback']
        
        data = {'name': name, 'email': email, 'feedback': feedback}

        return render(request, 'feedback/feedbackpost.html', {'data': data})
