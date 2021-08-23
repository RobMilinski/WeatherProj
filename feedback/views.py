from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ContactForm

# Add this view

def feedbackapp(request):
    if request.method == 'GET':
        #if page called from navbar, initial open
        return render(request, 'feedback/feedbackget.html')
    else:
        #when customer inputs feedback
        name = request.POST['customername']
        email = request.POST['customeremail']
        feedback = request.POST['customerfeedback']
        
        #create dictionary from customer inputs
        data = {'name': name, 'email': email, 'feedback': feedback}

        #display feedback on template page
        return render(request, 'feedback/feedbackpost.html', {'data': data})
