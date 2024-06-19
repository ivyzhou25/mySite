from django.db import models
from django import forms
from .models import Image

class ImageForm(forms.Form):        
    prompt = forms.CharField(label="Additional image information:", max_length=100)
    file = forms.FileField(label="Upload image:")
    
class CourseForm(forms.Form):        
    course1 = forms.CharField(label="Course 1:", max_length=15)
    course2 = forms.CharField(label="Course 2:", max_length=15)