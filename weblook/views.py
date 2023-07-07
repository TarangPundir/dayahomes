from django.shortcuts import render
from homeapp.models import *
from django.http import JsonResponse, HttpResponse

# Create your views here.

def home(request):
    banner = Banner.objects.all()
    employees = Employee.objects.all()
    return render(request, 'home.html', {'banner': banner, 'employees':employees})

def career(request):
    return render(request, 'career.html')

def jobFinds(request):
    search_term = request.POST.get('search_by_job')
    search_category = request.POST.get('search_by_category')
    jobs = Job.objects.filter(name__icontains=search_term, category__name__icontains=search_category)

    unique_jobs = {}
    
    for job in jobs:
        job_name = job.name
        if job_name not in unique_jobs:
            job_dict = {
                'name': job_name,
                'category': [category.name for category in job.category.all()],
                'salary': job.salary,
                'location': job.location
            }
            unique_jobs[job_name] = job_dict
    
    job_list = list(unique_jobs.values())
    
    return JsonResponse(job_list, safe=False)
