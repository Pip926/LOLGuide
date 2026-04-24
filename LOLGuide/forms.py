from django import forms  # type: ignore
from django.contrib.auth.models import User  # type: ignore
from django.contrib.auth.forms import UserCreationForm  # type: ignore

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email")


