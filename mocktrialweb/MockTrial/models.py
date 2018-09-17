from django.db import models
from django import forms
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify
#from djrichtextfield.models import RichTextField
import datetime

# Create your models here.
class Person(models.Model):
    name=models.TextField(null=True)
    emailAddress=models.EmailField(null=True)
    phoneNumber=models.TextField(null=True, blank=True)

class TeamMember(Person):
    dateJoined=models.DateField(auto_now_add=True)
    gradClass=models.CharField(max_length=4, null=True) 
    studies=models.TextField(null=True)
    linkedin=models.URLField(null=True, blank=True)
    photo=models.ImageField(upload_to='photos', null=True, blank=False)
    
    def __str__(self):
        return self.name
        
