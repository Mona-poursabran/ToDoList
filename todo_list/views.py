from operator import itemgetter
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from todo_list.forms import TodoForm
from .models import *


def homepage(request):
    list_todo = TODOList.objects.all()
    if request.method == 'POST':
        form = TodoForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, ('The item is addedd!'))
            return render(request, 'todo/home.html', {'todo': list_todo})
        else:
            messages.warning(request, ('The box is empty!'))
            return redirect('home')
    else:
        return render(request, 'todo/home.html', {'todo': list_todo})


def edit_item(request, item_id):
    todo_item = get_object_or_404(TODOList, id = item_id)
    if request.method == 'POST':
        form = TodoForm(request.POST or None, instance=todo_item)
        if form.is_valid():
            form.save()
            messages.success(request, ('The item is edited!!'))
            return redirect('home')
    else:
        return render(request, 'todo/update.html', {'todo': todo_item})


def delete_item(request):
    if request.POST.get('action') == 'post':
        task_id = int(request.POST.get('task_id'))
        todo = TODOList.objects.get(id=task_id)
        todo.delete()
        return JsonResponse({'success': True})


def delete_all(requset):
    todo = TODOList.objects.all()
    todo.delete()
    return JsonResponse({'success': True})


def delete_completed(request):
    todo = TODOList.objects.filter(complete = True)
    todo.delete()
    return JsonResponse({'success': True})


def cross_off(request, item_id):
    todo = TODOList.objects.get(id = item_id)
    todo.complete = True
    todo.save()
    return redirect('home')


def uncross(request, item_id):
    todo = TODOList.objects.get(id = item_id)
    todo.complete = False
    todo.save()
    return redirect('home')
