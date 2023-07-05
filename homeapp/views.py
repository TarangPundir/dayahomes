from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static

def home(request):
    return render(request, 'try.html')

def add_banner(request):
    return render(request, 'banner/create.html')

def save_banner(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        text = request.POST.get('text')
        image = request.FILES.get('image')

        # Create a new banner instance
        banner = Banner(name=name, text=text, image=image)
        banner.save()

        return HttpResponse('Banner saved successfully.')

    return HttpResponse('Invalid request.')

def index_banner(request):
    banner = Banner.objects.all()
    return render(request, 'banner/index.html', {'banner': banner})