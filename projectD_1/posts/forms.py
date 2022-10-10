from .models import Post, Group
from django.forms import ModelForm, TextInput, Textarea

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['name', 'text', 'producer', 'group']
        # fields = '__all__'
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название фильма'
            }),
            "producer": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Режиссер'
            }),
            "text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание'
            }),
            # "group": TextInput(attrs={
            #     'class': 'form-control',
            #     'placeholder': 'Жанр'
            # }),
        }




