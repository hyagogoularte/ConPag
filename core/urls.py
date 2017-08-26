from django.conf.urls import url

from core import views

urlpatterns = [
	url(r'^$', views.HomeView, name='home'),
	url(r'^lancamentos/$', views.LancamentoView, name='lancamentos'),
	url(r'^lancamentos/novo/$', views.NovoLancamentoView, name='novo-lancamento'),
	url(r'^lancamentos/(?P<id>[0-9]+)/editar/$', views.EditarLancamentoView, name='editar-lancamento'),
	url(r'^lancamentos/(?P<id>[0-9]+)/deletar/$', views.DeletarLancamentoView, name='deletar-lancamento'),

]