from django.shortcuts import render
from django.utils import timezone

from .models import MinUrl

def index(request):
	context = {}
	return render(request, 'add_url.html', context)

def add(request):
	min_url = MinUrl(url_base = request.POST['url-base'], add_at = timezone.now()) 
	min_url.save()
	context = {'min_url': 'test'}
	return render(request, 'min_url.html', context)