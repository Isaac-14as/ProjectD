# ice_cream/urls.py
from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    # Главная страница
    path('', views.index, name = 'main'),
    # Страницы сообществ
    path('groups/', views.groups, name = 'groups'),

    # path('group/<slug:slug>/', views.group_posts, name = 'group')
    
    path('group', views.group_posts, name = 'group')

] 