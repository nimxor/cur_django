from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse

from .models import Post

# Create your functional views here.

def post_create(request):
	return HttpResponse("<h1> Create </h1>")

def post_detail(request,id=None):
	instance = get_object_or_404(Post,id=id) # just a type of a query set 
	# instance = Post.object.get(id=3)
	context = {
	"title" : instance.title , 
	"inst" : instance
	}
	return render(request,"post_detail.html",context)

def post_list(request):
	obj=Post.objects.all() 
	context = {
	"object_list" : obj , 
	"title" : "list"
	}
	# if request.user.is_authenticated(): # will give weather the user is authenticated or not
	# 	context = {
	# 	"title" : "My list"
	# 	}
	# else:
	# 	context = {
	# 	"title" : "list"
	# 	}	
	return render(request,"index.html",context)
	# return HttpResponse("<h1> List </h1>")

def post_update(request):
	return HttpResponse("<h1> Update </h1>")

def post_delete(request):
	return HttpResponse("<h1> Delete </h1>")