from django.urls import path
from .views import MyRegister, Redirect


urlpatterns = [
    path('home/', MyRegister, name='register'),
    path('redirect/', Redirect, name='redirect')
]