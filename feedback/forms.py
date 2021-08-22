from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=500, label="Name")
    email = forms.EmailField(max_length=100, label="Email")
    comment = forms.CharField(max_length=200, label="Comment")
    