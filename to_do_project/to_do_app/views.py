from django.shortcuts import render, redirect, get_list_or_404
from to_do_app.models import task
from .form import task_form

# Create your views here.
def task_list(request):
    task_info = task.objects.all().order_by('-id')
    return render(request, 'task/task_list.html', {'task_info':task_info})

def home(request):
    if request.method == 'POST':
        form_data = task_form(request.POST)
        if form_data.is_valid():
            form_data.save()
            return redirect('task_list')
    else:
        myform = task_form()
    return render(request, 'task/home.html', {'data':myform})

def task_edit(request, pk):
    task_data = task.objects.get(id=pk)
    if request.method == 'POST':
        form = task_form(request.POST, instance=task_data)
        if form.is_valid():
            task_data.save()
            return redirect('task_list')
    else:
        form = task_form(instance=task_data)
    return render(request, 'task/task_edit.html', {'data':form, 'task_data':task_data})

def task_delete(request, pk):
    task_data = task.objects.get(id=pk)
    task_data.delete()
    return redirect('task_list')