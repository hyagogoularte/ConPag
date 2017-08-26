#forms.py

from django import forms
from django.contrib.auth.forms import AuthenticationForm 

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Usuário", max_length='30', 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Senha", max_length='30', 
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))





