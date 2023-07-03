from django.urls import path
from . import views
urlpatterns = [
    path('try', views.home, name='try'),
]