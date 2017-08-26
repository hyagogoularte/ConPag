#forms.py

from django import forms
from django.contrib.auth.forms import AuthenticationForm 
from core.models import Lancamento

class BootstrapModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BootstrapModelForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Usuário", max_length='30', 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Senha", max_length='30', 
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))


class LancamentoForm(BootstrapModelForm):
    class Meta:
        model = Lancamento
        fields = '__all__'
        exclude = ['usuario', 'estabelecimento']

    data_pagamento = forms.CharField(widget=forms.TextInput(attrs={'class':'datepciker'})),
    data_vencimento = forms.CharField(widget=forms.TextInput(attrs={'class':'datepciker'})),


