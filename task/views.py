from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Todo
from .forms import TodoForm

def todo_list(request):
    todos = Todo.objects.all()
    form = TodoForm()
    return render(request, 'todos/todo.html', {'todos': todos, 'form': form})


def add_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save()
            data = {'id': todo.id, 'task': todo.task}
            return JsonResponse(data)
        else:
            return JsonResponse({'error': 'Invalid form data'}, status=400)
    return JsonResponse({'error': 'Bad request'}, status=400)
