from django.urls import path, include
from todo.views import current_todos

urlpatterns = [
    path('current/', current_todos, name='current-todos'),
]
