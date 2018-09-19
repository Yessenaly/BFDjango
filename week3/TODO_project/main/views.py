from django.shortcuts import render
import datetime

# Create your views here.

from django.http import HttpResponse

def hello(request):
    html = "<html><body>Hello</body></html>"
    return HttpResponse(html)

def todo_list(request):
    tasks = ['task 1', 'task 2', 'task 3', 'task 4', 'task 5']
    created = datetime.datetime.now()
    due = datetime.datetime.now()
    todo_list = {
        'tasks': tasks,
        'created': created,
        'due': due,
        'owner': 'Admin',
        'status': 'Done'
    }

    return render(request, 'todo_list.html', todo_list)

def completed_todo_list(request):
    tasks = ['task 0']
    created = datetime.datetime.now()
    due = datetime.timedelta(days=2)
    completed_todo_list = {
        'tasks': tasks,
        'created': created,
        'due': due,
        'owner': 'Admin',
        'status': 'Not done'
    }
    return render(request , 'completed_todo_list.html' , completed_todo_list)
