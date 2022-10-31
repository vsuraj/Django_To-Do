from django.shortcuts import render, redirect, HttpResponse
from app.models import add_task
from app.form import task

# Create your views here.
def index(request):
    if request.method != 'POST':
        myform = task()
        return render(request, 'index.html', {'data':myform})
    else:
        form_data = task(request.POST)
        if form_data.is_valid():
            form_data.save()
            return redirect('list_task')
        else:
            return HttpResponse('something wrong')

def list_task(request):
    tasks = add_task.objects.all().order_by('-id')
    return render(request, 'list_tasks.html', {'tasks':tasks})

def edit_task(request, id):
    task_data = add_task.objects.get(id=id)
    if request.method != 'POST':
        form = task(instance=task_data)
        return render(request, 'task_edit.html', {'task':task_data})
    else:
        form = task(request.POST, instance=task_data)
        if form.is_valid():
            task_data.save()
            return redirect('list_task')
        
def delete_task(request, id):
    task_data = add_task.objects.get(id=id)
    task_data.delete()
    return redirect('list_task')