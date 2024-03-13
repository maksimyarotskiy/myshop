from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm


class SignUpForm(UserCreationForm):
    username = forms.CharField(label="Login")
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput())
    password2 = forms.CharField(label="Enter Password again", widget=forms.PasswordInput())

    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already in use.")
        return email

    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password1', 'password2')


class ProfileUserForm(forms.ModelForm):
    username = forms.CharField(disabled=True, label='login', widget=forms.TextInput())
    email = forms.CharField(disabled=True, label='email', widget=forms.TextInput())

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'address', 'phone_number']
        labels = {
            'address': 'Address',
            'phone_number': 'Phone_number',
        }
        widgets = {
            'address': forms.TextInput(),
            'phone_number': forms.TextInput(),
        }


