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


class LancamentoForm(BootstrapModelForm):
    class Meta:
        model = Lancamento
        fields = '__all__'
        exclude = ['usuario', 'estabelecimento']

class LancamentoDarBaixaForm(LancamentoForm):
    READONLY_FIELDS = ['titulo', 'descricao', 'valor', 'tipo_lancamento', 'data_vencimento']

    def __init__(self, readonly_form=False, *args, **kwargs):
        super(LancamentoForm, self).__init__(*args, **kwargs)
        if readonly_form:
            for field in self.READONLY_FIELDS:
                self.fields[field].widget.attrs['readonly'] = True

