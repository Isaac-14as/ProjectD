from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    template = 'posts/index.html'
    context = {
        'main_text' : 'Это главная страница проекта',
    }
    return render(request, template, context)

def groups(request):
    template = 'posts/group_list.html'
    return render(request, template)

def group_posts(request):
    template = 'posts/posts_group_posts.html'
    context = {
        'info' : 'Здесь будет информация о группах проекта'
    }
    return render(request, template, context)
