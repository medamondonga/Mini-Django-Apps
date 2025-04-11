from django.urls import path
from .views import todo, TestView, CreateTask, UpdateTask, DeleteTask

urlpatterns = [
    path("", todo, name='todo-list'),
    path("test/", TestView.as_view(), name="test"),
    path("create/", CreateTask.as_view(), name="create"),
    path("task/<int:pk>/update/", UpdateTask.as_view(), name="update"),
    path("task/<int:pk>/delete/", DeleteTask.as_view(), name="delete")
]
