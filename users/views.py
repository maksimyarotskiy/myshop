from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordResetConfirmView
from django.urls import reverse_lazy
from django.views import View
from django.shortcuts import render, redirect
from django import forms
from django.views.generic import CreateView, UpdateView

from .forms import SignUpForm, ProfileUserForm
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


class ProfileUser(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = ProfileUserForm
    template_name = 'profile.html'
    extra_context = {'title': 'Profile'}

    def get_success_url(self):
        return reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


