from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.contrib.auth.models import User
from core.models import Usuario, Estabelecimento, Lancamento
from lancamento.forms import LancamentoForm


@login_required(login_url="/")
def LancamentoView(request):
    usuario = pegarUsuario(request.user)
    estabelecimento = usuario.estabelecimento
    lancamentos = Lancamento.objects.filter(estabelecimento=estabelecimento)

    return render(request, 'home/index.html', {
                                                'estabelecimento': estabelecimento,
                                                    'lancamentos': lancamentos
                                            })


@login_required(login_url="/")
def NovoLancamentoView(request):
    if request.method != "POST":
        form = LancamentoForm()
        return render(request, 'lancamento/novo.html', {'form': form})
    
    form = LancamentoForm(request.POST)

    if form.is_valid():
        lancamento = form.save(commit=False)
        lancamento.usuario = pegarUsuario(request.user)
        lancamento.estabelecimento = pegarUsuario(request.user).estabelecimento
        lancamento.save()

        return redirect('lancamentos')


@login_required(login_url="/")
def EditarLancamentoView(request, id=None):
    try:
        instance = get_object_or_404(Lancamento, id = id)

        if request.method != "POST":
            form = LancamentoForm(instance=instance)
            return render(request, 'lancamento/editar.html', {'form': form})


        form = LancamentoForm(request.POST, instance=instance)

        if form.is_valid():
            lancamento = form.save(commit=False)
            lancamento.usuario = pegarUsuario(request.user)
            lancamento.estabelecimento = pegarUsuario(request.user).estabelecimento
            lancamento.save()

        return redirect('lancamentos')

    except Lancamento.DoesNotExist:
        raise Http404('Huston, we have a problem!')


@login_required(login_url="/")
def DeletarLancamentoView(request, id=None):
    try:
        instance = get_object_or_404(Lancamento, id = id)
        instance.delete()
        messages.success(request, "Deletado com sucesso!")
        return redirect('lancamentos')
    except Lancamento.DoesNotExist:
        raise Http404('Huston, we have a problem!')


@login_required(login_url="/")
def DarBaixaLancamentoView(request, id=None):
    try:
        instance = get_object_or_404(Lancamento, id = id)

        if request.method != "POST":
            form = LancamentoForm(instance=instance, readonly_form=True)
            return render(request, 'lancamento/editar.html', {'form': form})


        form = LancamentoForm(request.POST, instance=instance)

        if form.is_valid():
            form.save()

        return redirect('lancamentos')

    except Lancamento.DoesNotExist:
        raise Http404('Huston, we have a problem!')



def pegarUsuario(usuario):
    return Usuario.objects.get(usuario = usuario)
