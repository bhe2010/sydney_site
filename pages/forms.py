from socket import fromshare
from django import forms

class ContactForm(forms.Form):
    yourname = forms.CharField(max_length=100, label='Your name')
    email = forms.EmailField(label='Your e-mail address')
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)