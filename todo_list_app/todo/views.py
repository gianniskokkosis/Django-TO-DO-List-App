from django.shortcuts import render

def home(request):
    return render(request, 'todo/todo_home.html')


def about(request):
    return render(request, 'todo/todo_about.html')