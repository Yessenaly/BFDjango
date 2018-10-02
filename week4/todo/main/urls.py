from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello),
    path('completed_tasks' , views.completed_tasks),
    path('all_tasks' , views.all_tasks),
]