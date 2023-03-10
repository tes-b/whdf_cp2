from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from test_web.settings import AUTH_USER_MODEL

class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "password", "password_check", "email") 