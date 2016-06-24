from django.shortcuts import render
from django.http import HttpResponse

# Create your functional views here.

def post_home(request):
	return HttpResponse("<h1> Django </h1>")
