from django.urls import path
from . import views

urlpatterns = [
    path('todo/', views.todo_list, name='todo_list'),
    path('add-todo/', views.add_todo, name='add_todo'),
]
