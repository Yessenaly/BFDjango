from django.contrib import admin
from django.urls import path , include

from . import views

urlpatterns = [
    path('hello/', views.hello),
    path('todo_list/', views.todo_list),
    path('completed_todo_list/' , views.completed_todo_list)
]
