from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
	#return HttpResponse('Rango says: Hello world! <br/> <a href="/rango/about">About</a>')
	return HttpResponse("Rango says: Hello world! <br/> <a href='%s'>About</a>" %reverse('about'))

def about(request):
	#return HttpResponse('Rango says here is the about page. <br/> <a href="/rango/">Index</a>')
	return HttpResponse("<a href='%s'>Index</a>" %reverse('index'))