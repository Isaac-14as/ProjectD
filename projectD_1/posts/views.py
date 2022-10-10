from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Post, Group
from .forms import PostForm


def index(request):
    template = 'posts/index.html'
    posts = Post.objects.order_by('-name')[:10]
    context = {
        'posts' : posts,
    }
    return render(request, template, context)

def groups(request):
    template = 'posts/group_list.html'
    group = Group.objects.order_by()[:10]
    context = {
        'groups': group,
    }
    return render(request, template, context)

def group_posts(request, slug):
    amount = int(request.GET.get("amount", 5))
    template = 'posts/posts_group_posts.html'
     # Функция get_object_or_404 получает по заданным критериям объект 
    # из базы данных или возвращает сообщение об ошибке, если объект не найден.
    # В нашем случае в переменную group будут переданы объекты модели Group,
    # поле slug у которых соответствует значению slug в запросе

    group = get_object_or_404(Group, slug=slug)
 
    # Метод .filter позволяет ограничить поиск по критериям.
    # Это аналог добавления
    # условия WHERE group_id = {group_id}
    posts = Post.objects.filter(group=group).order_by('name')[:amount]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, template, context) 



def create_post(request):
    template = 'posts/create_post.html'
    error = ''
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')
        else:
            error = 'Форма была неверна'


    form = PostForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, template, data)

    
