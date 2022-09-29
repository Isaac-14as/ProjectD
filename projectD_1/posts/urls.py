# ice_cream/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Главная страница
    path('', views.index),
    # Страницы сообществ
    path('groups/', views.groups),

    path('group/<slug:slug>/', views.group_posts)

] 