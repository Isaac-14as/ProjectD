from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model() 

class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    # Параметр on_delete=models.CASCADE обеспечивает
    #  связность данных: если из таблицы User будет удалён 
    # пользователь, то будут удалены все связанные с ним посты.
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    ) 

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