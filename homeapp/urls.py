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
    path('banner/update', views.update_banner, name='update_banner')

]

