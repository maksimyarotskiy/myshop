from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views import View
from django.shortcuts import render, redirect
from django import forms
from django.views.generic import CreateView

from .forms import SignUpForm
from .models import UserProfile

class LoginUser(LoginView):
    template_name = 'registration/login.html'

class RegisterUser(CreateView):
    form_class = SignUpForm
    template_name = 'registration/signup.html'
    extra_context = {'title': "Registration"}
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)

        return response


