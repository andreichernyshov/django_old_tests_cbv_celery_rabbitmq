
import time
from django import forms


class ContactForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    when_to_do = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'form-control'}))


class StatusForm(forms.Form):
    redirekt = forms.URLField(widget=forms.URLInput(attrs={'class': 'form-control'}))
