from django.shortcuts import render
from blog.models import Article

def index(request):
    return render(request,'index.html',{})

# def blog(request):
#     return render(request,'blog.html',{})

def contact(request):
	return render(request,'contact.html',{})

def about(request):
	return render(request,'about.html',{})

def blog(request):
	posts = Article.objects.all()
	return render(request,'blog.html',{'posts':posts})


