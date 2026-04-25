from django import forms  # type: ignore
from django.contrib.auth.models import User  # type: ignore
from django.contrib.auth.forms import UserCreationForm  # type: ignore
from .models import Profile

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email")


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['favourite_champion', 'favourite_region', 'avatar', 'bio']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 3, 'placeholder': "Расскажи о себе..."}),
        }

        