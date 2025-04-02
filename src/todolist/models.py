"""
we create our models here
"""
from django.db import models

class Task(models.Model):
    """
    this is the model of our Tasks
    """
    name= models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"
    