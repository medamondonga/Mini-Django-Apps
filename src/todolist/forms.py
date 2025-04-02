"""
we'll create our forms here
"""
from django import forms
from.models import Task

class AddTask(forms.ModelForm):
    """
    the form of our task
    """
    class Meta:
        """
        the form of our task
        """
        model = Task
        fields = ("__all__")
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Ajouter une tache"}),
        }
