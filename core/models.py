from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Estabelecimento(models.Model):
    class Meta: 
        ordering: ('nome')

    nome = models.CharField(max_length=50)
    data_cadastro = models.DateTimeField(db_index=True, auto_now_add=True)
    data_atualizacao = models.DateTimeField(db_index=True, auto_now=True)

    def __str__(self):
        return self.nome 


class Usuario(models.Model):
    usuario = models.OneToOneField(User)
    estabelecimento = models.ForeignKey(Estabelecimento)


class TipoLancamento(models.Model):
    class Meta:
        ordering = ('data_cadastro', 'nome')

    nome = models.CharField(db_index=True, max_length=30, blank=False)
    data_cadastro = models.DateTimeField(db_index=True, auto_now_add=True)
    data_atualizacao = models.DateTimeField(db_index=True, auto_now=True)

    def __str__(self):
        return self.nome


# class Item(models.Model):
#     class Meta:
#         ordering = ('data_cadastro', 'nome')

#     nome = models.CharField(db_index=True, max_length=30, blank=False)
#     descricao = models.TextField(max_length=200)
#     data_cadastro = models.DateTimeField(db_index=True, auto_now_add=True)
#     data_atualizacao = models.DateTimeField(db_index=True, auto_now=True)

#     def __str__(self):
#         return self.nome


# class TipoPessoa(models.Model):
#     class Meta: 
#         ordering: ('nome')

#     nome = models.CharField(db_index=True, max_length=40, blank=False)
#     data_cadastro = models.DateTimeField(db_index=True, auto_now_add=True)
#     data_atualizacao = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.nome


class Conta(models.Model):
    class Meta:
        ordering = ('data_cadastro', 'nome')

    nome = models.CharField(max_length=30, blank=False)
    saldo = models.DecimalField(max_digits=25, decimal_places=2)
    estabelecimento = models.ForeignKey(Estabelecimento)
    data_cadastro = models.DateTimeField(db_index=True, auto_now_add=True)
    data_atualizacao = models.DateTimeField(db_index=True, auto_now=True)
    
    def __str__(self):
        return self.nome


class Lancamento(models.Model):
    class Meta:
        ordering = ('data_cadastro', 'titulo')

    titulo = models.CharField(max_length=40, blank=False)
    descricao = models.TextField(max_length=150, blank=True)
    valor = models.DecimalField(max_digits=25, decimal_places=2)
    estabelecimento = models.ForeignKey(Estabelecimento)
    usuario = models.ForeignKey(Usuario)
    tipo_lancamento = models.ForeignKey(TipoLancamento)
    data_vencimento = models.DateField(null=False, blank=True)
    data_pagamento = models.DateField(null=True, blank=True)
    data_cadastro = models.DateTimeField(db_index=True, auto_now_add=True)

    def __str__(self):
        return self.titulo


# class Pessoa(models.Model):
#     class Meta:
#         ordering: ('nome')

#     nome = models.CharField(max_length=40, blank=False)
#     telefone = models.TextField(blank=True)
#     id_tipo_pessoa = models.ForeignKey(TipoPessoa)
#     id_estabelecimento = 
#     data_cadastro = models.DateTimeField(db_index=True, auto_now_add=True)
#     data_atualizacao = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.nome