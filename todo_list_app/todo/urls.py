from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='todo-home'),
    path('about/',views.about, name='todo-about'),
    path('add_todo/', views.add_todo, name='add-todo'),
    path('delete_todo/<int:pk>/', views.delete_todo, name='delete-todo')
]