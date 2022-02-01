from django.shortcuts import render
from . models import Post

posts = [ 
	{
		'author': 'KP',
		'title': 'Blog 1',
		'content': 'KP works for Walmart',
		'date_posted': 'Jan 31, 2022',
	},
	{
		'author': 'JP',
		'title': 'Blog 2', 
		'content': 'JP works for Walmart',
		'date_posted': 'Jan 30, 2022',
	},
]

def home(request):
	context = {
		'posts' : Post.objects.all()
	}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})