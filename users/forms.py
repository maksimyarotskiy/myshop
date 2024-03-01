from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile


class SignUpForm(UserCreationForm):
    username = forms.CharField(label="Login")
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput())
    password2 = forms.CharField(label="Enter Password again", widget=forms.PasswordInput())

    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password1', 'password2')
