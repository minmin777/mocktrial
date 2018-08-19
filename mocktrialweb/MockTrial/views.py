from django.shortcuts import render
from MockTrial.models import *
from django.shortcuts import get_object_or_404
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from django.core.mail import BadHeaderError, EmailMessage
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings

def about(request):
	a = About.objects.first()
	return render(request, 'about.html', {'ab': a.about})

def team(request):
	team = TeamMembers.objects.all()
	return render(request, 'team.html', {'teams': team})

def home(request):
	return render(request, 'home.html')

def contact(request):
	info = Contact.objects.first()
	if request.method == 'GET':
		form = ContactForm()
	else:
		form = ContactForm(request.POST)
		if form.is_valid():
			contact_name = form.cleaned_data['contact_name']
			contact_email = form.cleaned_data['contact_email']
			content = form.cleaned_data['content']
			try:
				
				email = EmailMessage(contact_name, 
									content,
									contact_email,
									['Haverfordmocktrial@gmail.com'], #change to your email
									reply_to=[contact_email],
									)
				email.send()
				
				#send_mail(contact_name, content, settings.EMAIL_HOST_USER, [contact_email], fail_silently=False)
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect('/thanks/')
	return render(request, 'contact.html', {'info': info, 'form': form})

def thanks(request):
	info = Contact.objects.first()
	return render(request, 'thanks.html', {'info': info})
# Create your views here.
