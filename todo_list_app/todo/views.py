from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>TO-DO List App Home Page</h1>')


def about(request):
    return HttpResponse('<h1>TO-DO List App About Page</h1>')