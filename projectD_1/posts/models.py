from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model() 


class Group(models.Model):
    title = models.CharField(max_length=50)
    slug = models.TextField()
    description = models.TextField()

    
    def __str__(self):
        return self.title

class Post(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    # Параметр on_delete=models.CASCADE обеспечивает
    #  связность данных: если из таблицы User будет удалён 
    # пользователь, то будут удалены все связанные с ним посты.
    producer = models.CharField(max_length=100)
    group = models.ForeignKey(
        Group,  
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

# class PostFavorites(models.Model):
#     name = models.CharField(max_length=100)
#     text = models.TextField()
#     pub_date = models.DateTimeField(auto_now_add=True)
#     # Параметр on_delete=models.CASCADE обеспечивает
#     #  связность данных: если из таблицы User будет удалён 
#     # пользователь, то будут удалены все связанные с ним посты.
#     producer = models.CharField(max_length=100)
#     group = models.ForeignKey(
#         Group,
#         on_delete=models.CASCADE,
#         blank=True,
#         null=True
#     )



    
    

# Пробный вариант

# class Event(models.Model):
#     name = models.CharField(max_length=200)
#     start_at = models.DateTimeField(auto_now_add=True)
#     description = models.TextField()
#     contact = models.EmailField()
#     author = models.ForeignKey(
#         User,
#         on_delete=models.CASCADE,
#         related_name="events"
#     )
#     location = models.CharField(max_length=400)