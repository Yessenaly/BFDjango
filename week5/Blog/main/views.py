from django.shortcuts import render , redirect
import datetime

# Create your views here.

from django.http import HttpResponse
from django.http import Http404
from .models import Post , Comment

def hello(request):
    html = "<html><body>Hello</body></html>"
    return HttpResponse(html)

def all_posts(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request , 'post/all.html' , context)

