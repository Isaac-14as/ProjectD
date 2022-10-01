from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    template = 'posts/index.html'
    return render(request, template)

def groups(request):
    template = 'posts/posts_groups.html'
    return render(request, template)

def group_posts(request, slug):
    template = 'posts/posts_group_posts.html'
    return render(request, template)
