from django.shortcuts import render
from .models import TodoItem
from django.utils import timezone

def home(request):
    return render(request, 'todo/todo_home.html')


def about(request):
    return render(request, 'todo/todo_about.html')


def add_todo(request):
    return render(request, 'todo/todo_home.html')