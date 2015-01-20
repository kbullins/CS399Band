from django.shortcuts import render

def home(request):
	return render(request, 'index.html');

# Create custom views here
def theBand(request):
	return render(request, 'theBand.html');