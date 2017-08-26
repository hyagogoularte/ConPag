from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.contrib.auth.models import User
from core.models import Usuario, Estabelecimento, Lancamento, Conta

# Create your views here.
@login_required(login_url="/")
def HomeView(request):

    if request.user.is_superuser:
        lancamentos = Lancamento.objects.all()
        contas = Conta.objects.all()
        return render(request, 'home/index.html', {'lancamentos': lancamentos, 'contas': contas})

    usuarioObj = Usuario.objects.get(usuario=request.user)
    estabelecimento = usuarioObj.estabelecimento
    conta = Conta.objects.get(estabelecimento=estabelecimento)
    lancamentos = Lancamento.objects.filter(estabelecimento=estabelecimento)

    return render(request, 'home/index.html', {'estabelecimento': estabelecimento, 'lancamentos': lancamentos, 'conta': conta})