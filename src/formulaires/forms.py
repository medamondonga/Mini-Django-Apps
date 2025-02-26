from django import forms

from formulaires.models import Register


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields= '__all__'
        exclude = ['faculty']
        widgets = {'date_of_birth': forms.DateInput(attrs={'type': 'date'})}
