from django.contrib import admin
from django.contrib.admin.options import ModelAdmin

from core.models import Usuario, Estabelecimento, Lancamento, Conta, TipoLancamento#, Item, TipoPessoa, Pessoa

# class TipoPessoa(ModelAdmin):
# 	list_display = (nome)

#remover 
admin.site.register(Usuario)
admin.site.register(Estabelecimento)
admin.site.register(Lancamento)
admin.site.register(Conta)
admin.site.register(TipoLancamento)
# admin.site.register(Pessoa)
# admin.site.register(TipoPessoa)
# admin.site.register(Item)
