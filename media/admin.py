from django.contrib import admin
from .models import media

# Register your models here.
class mediaadmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'logo']

admin.site.register(media, mediaadmin)