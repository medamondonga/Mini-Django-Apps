from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from formulaires.forms import RegisterForm
from formulaires.models import Register


def Redirect(request):
    return render(request, "formulaires/redirect.html")

def MyRegister(request):
    if request.method == "POST":
        register = RegisterForm(request.POST)
        if register.is_valid():
            email = register.cleaned_data.get('email')
            if Register.objects.filter(email=email).exists():
                print("le mail existe deja")
                register = RegisterForm()
                return render(request, "formulaires/register.html", {"register": register})

            else:
                register.save()
        return redirect(Redirect)
    else:
        register = RegisterForm()

    return render(request, "formulaires/register.html", {"register": register})

