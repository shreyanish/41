from django.contrib import admin
from .models import tech

# Register your models here.
class techadmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'logo']

admin.site.register(tech, techadmin)