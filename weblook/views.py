from django.shortcuts import render
from homeapp.models import *

# Create your views here.

def home(request):
    banner = Banner.objects.all()
    employees = Employee.objects.all()
    return render(request, 'home.html', {'banner': banner, 'employees':employees})