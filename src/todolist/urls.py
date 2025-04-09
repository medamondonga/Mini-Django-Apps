from django.urls import path
from .views import todo, test

urlpatterns = [
    path("", todo, name='todo-list'),
    path("test/", test, name="test")
]
