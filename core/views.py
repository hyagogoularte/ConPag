from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from core.models import Usuario, Estabelecimento, Lancamento
from django.contrib.auth.models import User
from core.forms import LancamentoForm

# Create your views here.
@login_required(login_url="/")
def HomeView(request):
	usuario = Usuario.objects.get(usuario = request.user)
	estabelecimento = usuario.estabelecimento
	lancamentos = Lancamento.objects.filter(estabelecimento=estabelecimento)
	return render(request, 'home/index.html', {
		'estabelecimento': estabelecimento,
		'lancamentos': lancamentos})

@login_required(login_url="/")
def LancamentoView(request):
	form = LancamentoForm()
	return render(request, 'home/lancamento.html', {'form': form})
