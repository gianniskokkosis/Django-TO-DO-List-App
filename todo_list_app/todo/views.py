from django.shortcuts import render
from .models import TodoItem
from django.http import HttpResponseRedirect

def home(request):
    context = {
        'todos': TodoItem.objects.all().order_by('-date_added')
    }
    return render(request, 'todo/todo_home.html', context)


def about(request):
    return render(request, 'todo/todo_about.html')


def add_todo(request):
    content = request.POST['todo']
    create_obj = TodoItem.objects.create(content=content)
    print(create_obj.content)
    return HttpResponseRedirect('/')

def delete_todo(request, pk):
    TodoItem.objects.get(id=pk).delete()
    return HttpResponseRedirect('/')