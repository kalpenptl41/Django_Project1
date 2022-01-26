from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
	return HttpResponse("<h1>Hello Python_Web2 Home</h1>")

def about(request):
	return HttpResponse("<h1>Hello Python_Web2 About</h1>")
