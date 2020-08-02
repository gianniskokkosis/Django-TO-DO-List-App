from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'todo/todo_home.html')


def about(request):
    return HttpResponse('<h1>TO-DO List App About Page</h1>')