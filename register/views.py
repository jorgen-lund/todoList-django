from django.shortcuts import render, redirect
from .forms import RegisterForm
# Using RegisterForm as opposed to django form,
# as it is used in forms.py already


def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        #Installing crispy-forms library to style
        return redirect("/")
    else:
        form = RegisterForm()
        

    
    return render(response, "register/register.html", {"form":form})