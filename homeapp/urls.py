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
    
    path('category/add', views.add_category, name='add_category'),
    path('category/save', views.save_category, name='save_category'),
    path('category/list', views.list_category, name='list_category'),
    path('category/delete/<int:id>', views.delete_category, name='delete_category'),
    path('category/edit/<int:id>', views.edit_category, name='edit_category'),
    path('category/update', views.update_category, name='update_category'),
    
    path('job/add', views.add_job, name='add_job'),
    path('job/save', views.save_job, name='save_job'),
    path('job/index', views.index_job, name='index_job'),
    path('job/edit/<int:id>', views.edit_job, name='edit_job'),
    path('job/delete/<int:id>', views.delete_job, name='delete_job'),
    path('job/update', views.update_job, name='update_job')

]

