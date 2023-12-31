from django.db import models

# Create your models here.

class Banner(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to= 'banner', blank=False, null=True)
    text = models.CharField(max_length=200)
    
class Employee(models.Model):
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=12)
    image = models.ImageField(upload_to='employee', blank=False, null=True)
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Job(models.Model):
    name = models.CharField(max_length=50)
    category = models.ManyToManyField('Category')
    salary = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
