from django.db import models
from django import forms
from .models import Image

class ImageForm(forms.Form):        
    prompt = forms.CharField(label="Additional image information:", max_length=100)
    file = forms.FileField(label="Upload image:")
    
