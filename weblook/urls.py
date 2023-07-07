from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='homepage'),
    path('career', views.career, name='career'),
    path('job/find', views.jobFinds, name="jobs_finds")
]

