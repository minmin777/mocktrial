from django.db import models
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify
#from djrichtextfield.models import RichTextField
import datetime


class About(models.Model):
	about = RichTextField()
	def __str__(self):
		return "About"

class FAQ(models.Model):
	question = models.CharField(max_length=30)
	answer = models.CharField(max_length=200)
	def __str__(self):
		return self.question

class TeamMembers(models.Model):
	photo = models.ImageField(upload_to='photos/')
	name = models.CharField(max_length=30)
	description = RichTextField()
	linkedin = models.URLField(blank=True, null=True)
# Create your models here.
