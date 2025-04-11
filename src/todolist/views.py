"""
here we create our views
"""
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from .models import Task
from .forms import AddTask
from django.urls import reverse_lazy


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


class TestView(ListView):
    """
    here we test our CVB
    """
    model = Task
    template_name = "todolist/test.html"

class CreateTask(CreateView):
    """
    This CVB help us to create a task
    """
    model = Task
    template_name="todolist/todo.html"
    form_class = AddTask
    success_url = reverse_lazy("test")
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["soumission"] = "Ajouter"
        return context

class UpdateTask(UpdateView):
    model = Task
    template_name= "todolist/todo.html/"
    form_class = AddTask
    success_url= reverse_lazy("test")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["soumission"] = "Modifier"
        return context

class DeleteTask(DeleteView):
    model = Task
    template_name="todolist/todo.html"
    success_url= reverse_lazy("test")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['soumission'] = "Supprimer"
        return context