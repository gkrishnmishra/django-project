from django.shortcuts import render,redirect,get_object_or_404
from .models import *
# Create your views here.

def index(request):
    if request.method=='POST':
        task_title=request.POST.get('title')
        task_status=request.POST.get('complete')
        if task_status == 'on':
            is_completed=True
        else:
            is_completed=False
            

        task.objects.create(
            title=task_title,
            complete=is_completed
        )
        return redirect('index')



    tasks=task.objects.all()
    return render (request,'todotask/list.html',{'tasks':tasks} )



def update_task(request, id):
    task_obj = task.objects.get(id=id)
    if request.method == 'POST':
        task_obj.title = request.POST.get('title')
        task_obj_status = request.POST.get('complete')

        if task_obj_status == 'on':
            is_completed = True
        else:
            is_completed = False

        task_obj.complete = is_completed
        task_obj.save()
        return redirect('index')

    return render(request, 'todotask/update.html', {'task': task_obj})

def deleteTask(request, pk):
    task_obj = get_object_or_404(task, id=pk)
    if request.method == 'POST':
        task_obj.delete()
        return redirect('index')
    return render(request, 'todotask/delete.html', {'task': task_obj})
