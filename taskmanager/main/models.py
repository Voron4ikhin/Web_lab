from django.db import models

# Create your models here.


class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание', max_length=110)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/'

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


class Review(models.Model):
    review = models.TextField('')
