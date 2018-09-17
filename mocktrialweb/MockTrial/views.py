from django.shortcuts import render
from MockTrial.models import *
from django.shortcuts import get_object_or_404
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from django.core.mail import BadHeaderError, EmailMessage
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

