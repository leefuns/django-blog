from django.shortcuts import render
from blog.models import Article, Banner
from blog.forms import ContactForm
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger

def index(request):
	banner_list = Banner.objects.all()
	posts_1 = Article.objects.order_by("-id")[0]
	posts_2 = Article.objects.order_by("-id")[1]
	return render(request,'index.html',locals())


def contact(request):
	if request.method == 'POST':
		f = ContactForm(request.POST)
		if f.is_valid():
	 		data = f.cleaned_data
	 		f.save()
	else:
		f = ContactForm()
	return render(request,'contact.html',{'f':f})

def about(request):
	return render(request,'about.html',{})

def blog(request):
	posts = Article.objects.all()
	paginator = Paginator(posts,3)
	try:
		page = int(request.GET.get('page', 1))
		posts = paginator.page(page)
	except (EmptyPage, InvalidPage, PageNotAnInteger):
		posts = paginator.page(1)
	return render(request,'blog.html',locals())

def article(request,pk):
	art = Article.objects.order_by("id")[int(pk)-1]
	title = art.title
	content = art.content
	img = art.psot_img
	return render(request,'blog_article.html',locals())


