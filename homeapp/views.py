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
        
        return HttpResponse('saved successfully')

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



def add_employee(request):
    return render(request, 'employee/create.html')

def save_employee(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        contact = request.POST.get('contact')
        image = request.FILES.get('image')

        # Create a new banner instance
        employee = Employee(name=name, contact=contact, image=image)
        employee.save()
        return HttpResponse('saved successfully')

    return HttpResponse('Invalid request.')

def list_employee(request):
    employee = Employee.objects.all()
    return render(request, 'employee/list.html', {'employee': employee})

def delete_employee(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('list_employee')

def edit_employee(request, id):
    employee = Employee.objects.get(id=id)
    return render(request, 'employee/edit.html', {'employee': employee})

def update_employee(request):
    employee_id = request.POST.get('id')
    employee = Employee.objects.get(id=employee_id)
    name = request.POST.get('name')
    contact = request.POST.get('contact')
    image_file = request.FILES.get('image')
    
    if image_file:
        employee.image = image_file

    employee.name = name
    employee.contact = contact
    employee.save()
    return HttpResponse("Employee updated successfully.")


def add_category(request):
    return render(request, 'category/create.html')

def save_category(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        place = request.POST.get('place')
        category = Category(name=name, place=place)
        category.save()
        return HttpResponse('Created Successfully')
    return HttpResponse('Invalid Request')

def list_category(request):
    category = Category.objects.all()
    return render(request, 'category/index.html', {'category': category})

def delete_category(request, id):
    category = Category.objects.get(id=id)
    category.delete()
    return redirect('list_category')

def edit_category(request, id):
    category = Category.objects.get(id=id)
    return render(request, 'category/edit.html', {'category': category})
    
def update_category(request):
    category_id = request.POST.get('id')
    category = Category.objects.get(id=category_id)
    name = request.POST.get('name')
    place = request.POST.get('place')
    category.name = name
    category.place = place
    category.save()
    return HttpResponse('Updated Successfully')

def add_job(request):
    category = Category.objects.all()
    return render(request, 'job/create.html', {'category': category})

def save_job(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        category_ids = request.POST.getlist('category')
        categories = Category.objects.filter(id__in=category_ids)
        salary = request.POST.get('salary')
        location = request.POST.get('location')

        job = Job(name=name, salary=salary, location=location)
        job.save()
        job.category.set(categories)  # Set the many-to-many relationship

        return HttpResponse('Created Successfully')

    return HttpResponse('Error Occurred')

def index_job(request):
    job = Job.objects.all()
    return render(request, 'job/index.html', {'job': job})

def edit_job(request, id):
    job = Job.objects.get(id=id)
    category = Category.objects.all()
    return render(request, 'job/edit.html', {'job':job, 'category': category})

def delete_job(request, id):
    job = Job.objects.get(id=id)
    job.delete()
    return redirect('index_job')

def update_job(request):
    job_id = request.POST.get('id')
    job = Job.objects.get(id=job_id)
    name = request.POST.get('name')
    category_ids = request.POST.getlist('category')
    categories = Category.objects.filter(id__in=category_ids)
    salary = request.POST.get('salary')
    location = request.POST.get('location')
    
    job.name = name
    job.salary = salary
    job.location = location
    job.category.set(categories) 
    
    job.save()
    
    return HttpResponse('Updated Successfully')
    