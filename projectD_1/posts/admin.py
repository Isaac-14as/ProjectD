from django.contrib import admin
# Из модуля models импортируем модель Post
from .models import Post, Group

class PostAdmin(admin.ModelAdmin):
    # Перечисли поля, которые должны отображаться в админке
    list_display = ('pk', 'name', 'text', 'producer', 'group')
    #  Это позволит изменять поле group в любом 
    # посте без лишних движений мышкой, прямо из списка постов.
    list_editable = ('group',)
    # Добавляем интерфейс для поиска по тексту постов
    search_fields = ('name', 'text')

    # Это свойство сработает для всех колонок: где пусто — там будет эта строка 
    empty_value_display = '-пусто-'

# При регистрации модели Post источником конфигурации для неё назначем
#  класс PostAdmin
admin.site.register(Post, PostAdmin)
admin.site.register(Group)

