from django.shortcuts import render
import datetime

# Create your views here.

from django.http import HttpResponse
from .models import Task,Owner

def hello(request):
    html = "<html><body>Hello</body></html>"
    return HttpResponse(html)

def all_tasks(request):
    tasks = Task.objects.all()

    todo_list = {
        'tasks': tasks
    }

    return render(request, 'todo_list.html', todo_list)

def completed_tasks(request):
    tasks = Task.objects.filter(done_status = True)

    todo_list = {
        'tasks': tasks
    }

    return render(request, 'completed_todo_list.html', todo_list)

