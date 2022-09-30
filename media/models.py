from unicodedata import name
from django.db import models

# Create your models here.
class media(models.Model):
    name = models.CharField(max_length=120)
    logo = models.ImageField(upload_to='static/media-logos' ,null=True, blank=True)