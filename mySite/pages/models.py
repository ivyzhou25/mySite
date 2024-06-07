from django.db import models
import requests

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
