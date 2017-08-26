from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.contrib.auth.models import User
from core.models import Usuario, Estabelecimento, Lancamento

# Create your views here.
@login_required(login_url="/")
def HomeView(request):
    usuario = pegarUsuario(request.user)
    estabelecimento = usuario.estabelecimento
    lancamentos = Lancamento.objects.filter(estabelecimento=estabelecimento)

    return render(request, 'home/index.html', {
                                                'estabelecimento': estabelecimento,
                                                    'lancamentos': lancamentos
                                            })
def pegarUsuario(usuario):
    return Usuario.objects.get(usuario = usuario)