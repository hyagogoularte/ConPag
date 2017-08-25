#forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm 
from core.models import Lancamento

class BootstrapModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BootstrapModelForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control 123'
            })

# If you don't do this you cannot use Bootstrap CSS
class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Usuário", max_length='30', 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Senha", max_length='30', 
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))


class LancamentoForm(BootstrapModelForm):
	# titulo = models.CharField(max_length=40, blank=False)
 #    descricao = models.TextField(max_length=150, blank=True)
 #    valor = models.DecimalField(max_digits=25, decimal_places=2)
 #    estabelecimento = models.ForeignKey(Estabelecimento)
 #    usuario = models.ForeignKey(Usuario)
 #    tipo_lancamento = models.ForeignKey(TipoLancamento)
 #    data_vencimento = models.DateField(null=False, blank=True)
 #    data_pagamento = models.DateField(null=True, blank=True)
 #    data_cadastro = models.DateTimeField(db_index=True, auto_now_add=True)
	class Meta:
		model = Lancamento
		fields = ['titulo', 'descricao', 'valor', 'tipo_lancamento', 'data_vencimento', 'data_pagamento']

