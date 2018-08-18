from django.shortcuts import render
from MockTrial.models import *
from django.shortcuts import get_object_or_404
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector


def about(request):
	a = About.objects.first()
	return render(request, 'about.html', {'ab': a.about})

def team(request):
	team = TeamMembers.objects.all()
	return render(request, 'team.html', {'teams': team})
# Create your views here.
