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

    return HttpResponse('Invalid request.')

def index_banner(request):
    banner = Banner.objects.all()
    return render(request, 'banner/index.html', {'banner': banner})

def delete_banner(request, id):
    banner = Banner.objects.get(id=id)
    banner.delete()
    return redirect('index_banner')

def edit_banner(request, id):
    banner = Banner.objects.get(id=id)
    return render(request, 'banner/edit.html', {'banner': banner})

def update_banner(request):
    banner_id = request.POST.get('id')
    banner = Banner.objects.get(id=banner_id)
    name = request.POST.get('name')
    text = request.POST.get('text')
    image_file = request.FILES.get('image')
    
    if image_file:
        banner.image = image_file

    banner.name = name
    banner.text = text
    banner.save()
    return HttpResponse("Banner updated successfully.")

    