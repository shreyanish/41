from django.shortcuts import render, redirect
from tech.models import tech
from media.models import media

def homeview(request):
    tech_list = tech.objects.all()
    media_list = media.objects.all()
    context = {
        'tech_list': tech_list,
        'media_list': media_list,
    }
    return render(request, 'homeview.html', context)