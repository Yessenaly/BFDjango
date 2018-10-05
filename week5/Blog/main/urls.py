from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello),
    path('all_posts' , views.all_posts , name = "all_posts"),
]