from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        # Has to be named meta
        # Saves it into the same form as the used form.
        model = User
        #We are changing the User model when we use this form. 
        fields = ["username", "email", "password1", "password2"]
        # Will layout where the fields will be, in chosen order.
 