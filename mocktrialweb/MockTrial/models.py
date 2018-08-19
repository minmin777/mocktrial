from django.db import models
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify
#from djrichtextfield.models import RichTextField
import datetime


class About(models.Model):
	about = RichTextField()
	def __str__(self):
		return "About"

class Contact(models.Model):
	about = RichTextField()
	def __str__(self):
		return "Contact"

class FAQ(models.Model):
	question = models.CharField(max_length=30)
	answer = models.CharField(max_length=200)
	def __str__(self):
		return self.question

class TeamMembers(models.Model):
	photo = models.ImageField(upload_to='photos/')
	name = models.CharField(max_length=30)
	classnum = models.CharField(max_length=100)
	major = models.CharField(max_length=100)
	description = RichTextField()
	linkedin = models.URLField(blank=True, null=True)

	def __unicode__(self):
		return self.name; 
# Create your models here.
