from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db.models.base import Model
from django.forms import fields
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password = forms.CharField(max_length=10, required=True, label="Introduce a password", widget=forms.PasswordInput)
    password_confirmation = forms.CharField(max_length=10, required=True, label="Repeat the password", widget=forms.PasswordInput)

class Meta:
    Model = User
    fields = {"username", "email", "password", "password_confirmation"}
    help_texts = {k:"" for k in fields}
