from django import forms
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class" : "form-control",
        "id" : "username",
        "name": "username",
        "placeholder" : "Enter your username"
    }))