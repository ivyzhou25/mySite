from django.db import models
from django import forms
from .models import Image

class ImageForm(forms.Form):        
    prompt = forms.CharField(label="Additional image information:", max_length=100)
    file = forms.FileField(label="Upload image:")
    
class CourseForm(forms.Form):        
    query = forms.CharField(label="Question", widget=forms.Textarea(attrs={'cols':110}))
    
class ContactForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={"placeholder": "Your email"}))
    subject = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Subject"}))
    message = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Your message"}))