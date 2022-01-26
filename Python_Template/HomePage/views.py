from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
	return HttpResponse("<h1>Hello Home today is January 25th</h1>")

def about(request):
	return HttpResponse("<h1>Hello About it's a day before India's republic day celebration</h1>")