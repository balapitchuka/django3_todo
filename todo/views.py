from django.shortcuts import render
from todo.models import Todo

def current_todos(request):
    return render(request, 'todo/current_todos.html')
