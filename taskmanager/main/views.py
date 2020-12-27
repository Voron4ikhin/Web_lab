from django.shortcuts import render, redirect
from django.views.generic import DeleteView, DeleteView, UpdateView

from .models import Task

from .forms import TaskForm, ContactForm
from django.core.mail import send_mail

from django.contrib import messages

# Create your views here.


def index(request):
    tasks = Task.objects.order_by('id')
    return render(request, 'main/index.html', {'title': 'Заметки', 'tasks': tasks})


def about(request):
    return render(request, 'main/about.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)


def review(request):
    error = ''
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            mail = send_mail('Отзыв c сайта Curochka Production', form.cleaned_data['review'],
                      'checkw3b@yandex.ru', ['voron.ilya16@gmail.com'], fail_silently= False)
            if mail:
                return redirect('home')
            else:
                error = 'Ошибка отправки'
        else:
            error = 'Ошибка отправки'
    else:
        form = ContactForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/review.html', context)


def test1(request):
    return render(request, 'main/test1.html')


class TaskDetailView(DeleteView):
    model = Task
    template_name = 'main/detail_view.html'
    context_object_name = 'tasker'
    success_url = '/'


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'main/task_delete.html'
    success_url = '/'


class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'main/create.html'
    form_class = TaskForm


