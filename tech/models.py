from django.db import models

# Create your models here.
class tech(models.Model):
    name = models.CharField(max_length=120)
    logo = models.ImageField(upload_to='static/tech-logos' ,null=True, blank=True)