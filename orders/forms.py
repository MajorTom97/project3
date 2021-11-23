from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db.models.base import Model
from django.forms import fields
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=20, required=True, label="Enter Username")
    email = forms.EmailField()
    password1 = forms.CharField(max_length=10, required=True, label="Type a password", widget=forms.PasswordInput)
    password2= forms.CharField(max_length=10, required=True, label="Repeat the password", widget=forms.PasswordInput)

    class Meta:
        Model = User
        fields = {"username", "email", "password1", "password2"}
        
