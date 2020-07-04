from django.shortcuts import render, redirect
from django.utils import timezone
from .models import *
from django.http import HttpResponse
from .forms import *
from django.contrib.auth.decorators import login_required
from .decorators import *

# Create your views here.
@login_required(login_url='account_login')
def index(request):
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save()
        return redirect('todo:todolist')


    context = {
        'title': 'This is my Todo List',
        'tasks': tasks,
        'form': form
    }
    return render(request, 'todo/index.html', context)

@login_required(login_url='account_login')
@allowed_users(allowed_roles=['admin'])
def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('todo:todolist')

    context = {
        'title': 'Update' '' f" '{task}'",
        'form': form
    }
    return render(request, 'todo/update_task.html', context)

@login_required(login_url='account_login')
@allowed_users(allowed_roles=['admin'])
def deleteTask(request, pk):
    item = Task.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('todo:todolist')
    context ={
        'item': item
    }
    return render(request, 'todo/delete.html', context)