from django.shortcuts import render

def todo(request):
    """
    here we return our app
    """
    return render(request, 'todolist/todo.html')