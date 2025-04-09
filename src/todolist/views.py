"""
here we create our views
"""
from django.shortcuts import render
from .forms import AddTask

def todo(request):
    """
    here we return our app
    """
    if request.method == "POST":
        task = AddTask(request.POST)
        if task.is_valid():
            task.save()
            task = AddTask()
            #return render(request, "todolist/todo.html",{"task": task})
        else:
            print("Erreur")
    else:
        task = AddTask()
    return render(request, 'todolist/todo.html', {"task": task})

def test(request):
    return render(request, "todolist/test.html")