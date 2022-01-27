from django.shortcuts import render

posts = [ 
	{
		'Name':'KP',
		'Month':'Jan',
		'Date':'31',
		'Year':'2021',
		'Work':'KP works for Walmart' 
	},
	{
		'Name':'JP',
		'Month':'Jan',
		'Date':'30',
		'Year':'2020',
		'Work':'JP works for Target' 
	},
]

def home(request):
	context = {
		'posts' : posts
	}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})