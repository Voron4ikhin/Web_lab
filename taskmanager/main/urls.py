from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path('about', views.about, name = 'about'),
    path('create', views.create, name = 'create'),
    path('review', views.review, name = 'review'),
    path('test1', views.test1, name = 'test1'),
    path('<int:pk>', views.TaskDetailView.as_view(), name='detail_task'),
    path('<int:pk>/update_task', views.TaskUpdateView.as_view(), name='update_task'),
    path('<int:pk>/delete_task', views.TaskDeleteView.as_view(), name='delete_task'),
]