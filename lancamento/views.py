from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from pdb import set_trace as bp


from django.contrib.auth.models import User
from core.models import Usuario, Estabelecimento, Lancamento, Conta
from lancamento.forms import LancamentoForm, LancamentoDarBaixaForm


@login_required(login_url="/")
def LancamentoView(request):
    return redirect('home')


@login_required(login_url="/")
def NovoLancamentoView(request):
    if request.method != "POST":
        form = LancamentoForm()
        return render(request, 'lancamento/novo.html', {'form': form})
    
    form = LancamentoForm(request.POST)

    if form.is_valid():
        usuarioObj = Usuario.objects.get(usuario=request.user)

        lancamento = form.save(commit=False)
        if lancamento.valor < 0:
            messages.warning(request, "O valor do lançamento não pode ser negativo.")
            return render(request, 'lancamento/novo.html', {'form': form})

        lancamento.usuario = usuarioObj
        lancamento.estabelecimento = usuarioObj.estabelecimento
        lancamento.save()

        return redirect('lancamentos')
    else:
        messages.info(request, "Problema ao enviar o formulário!")
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
            usuarioObj = Usuario.objects.get(usuario=request.user)

            lancamento = form.save(commit=False)
            if lancamento.valor < 0:
                messages.warning(request, "O valor do lançamento não pode ser negativo.")
                return render(request, 'lancamento/novo.html', {'form': form})

            lancamento.usuario = usuarioObj
            lancamento.estabelecimento = usuarioObj.estabelecimento
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
        
        return redirect('home')
    except Lancamento.DoesNotExist:
        raise Http404('Huston, we have a problem!')


@login_required(login_url="/")
def DarBaixaLancamentoView(request, id=None):
    try:
        instance = get_object_or_404(Lancamento, id = id)

        if request.method != "POST":
            form = LancamentoDarBaixaForm(instance=instance, readonly_form=True)
            return render(request, 'lancamento/editar.html', {'form': form})


        form = LancamentoForm(request.POST, instance=instance)

        if form.is_valid():
            usuarioObj = Usuario.objects.get(usuario=request.user)
            conta = Conta.objects.get(estabelecimento=usuarioObj.estabelecimento)

            lancamento = form.save(commit=False)
            
            if conta.saldo < lancamento.valor:
                messages.warning(request, "O valor para ser lançando, não pode ser maior que tem na conta.")
                return render(request, 'lancamento/novo.html', {'form': form})

            saldoTemp = conta.saldo - lancamento.valor
            updated = Conta.objects.filter(id=conta.id).update(saldo=saldoTemp)

            if not updated:
                messages.warning(request, "O valor da conta não pode ser atualizado, contate o administrador.")
                return render(request, 'lancamento/novo.html', {'form': form})           

            form.save()

        return redirect('lancamentos')

    except Lancamento.DoesNotExist:
        raise Http404('Huston, we have a problem!')


