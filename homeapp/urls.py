from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('try', views.home, name='try'),
    path('banner/add', views.add_banner, name='add_banner'),
    path('banner/save', views.save_banner, name='save_banner'),
    path('banner/index', views.index_banner, name='index_banner'),
    path('banner/delete/<int:id>', views.delete_banner, name='delete_banner'),
    path('banner/edit/<int:id>', views.edit_banner, name='edit_banner'),
    path('banner/update', views.update_banner, name='update_banner'),
    path('employee/add', views.add_employee, name='add_employee'),    
    path('employee/save', views.save_employee, name='save_employee'),    
    path('employee/list', views.list_employee, name='list_employee'),    
    path('employee/delete/<int:id>', views.delete_employee, name='delete_employee'),    
    path('employee/update', views.update_employee, name='update_employee'),    
    path('employee/edit/<int:id>', views.edit_employee, name='edit_employee'),




]

