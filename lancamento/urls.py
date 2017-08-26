from django.conf.urls import url

from lancamento import views

urlpatterns = [
	url(r'^$', views.LancamentoView, name='lancamentos'),
	url(r'^novo/$', views.NovoLancamentoView, name='novo-lancamento'),
	url(r'^(?P<id>[0-9]+)/editar/$', views.EditarLancamentoView, name='editar-lancamento'),
	url(r'^(?P<id>[0-9]+)/deletar/$', views.DeletarLancamentoView, name='deletar-lancamento'),
	url(r'^(?P<id>[0-9]+)/dar-baixa/$', views.DarBaixaLancamentoView, name='lancamento-baixo'),

]