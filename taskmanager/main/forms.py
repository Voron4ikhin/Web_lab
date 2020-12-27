from .models import Task, Review
from django import forms
from django.forms import ModelForm, TextInput, Textarea


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task"]
        widgets = {
            "title": TextInput(attrs={
                'placeholder': 'Введите название',

            }),
            "task": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            }),
        }


class ContactForm(ModelForm):
    class Meta:
        model = Review
        fields = ["review"]
        widgets = {
            "review": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Напишите отзыв',
                'rows': 5,
            }),
        }
