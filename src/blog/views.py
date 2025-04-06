"""
Here we create our views
"""
from django.shortcuts import render

def home(request):
    """
    this views return our home page
    """
    return render(request, "blog/blog.html")