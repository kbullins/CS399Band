from django.shortcuts import render

def home(request):
	return render(request, 'index.html');

# Create custom views here
def theBand(request):
	return render(request, 'theBand.html');

def music(request):
	return render(request, 'music.html');

def tour(request):
	return render(request, 'tour.html');

def news(request):
	return render(request, 'news.html');