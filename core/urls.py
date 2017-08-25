from django.conf.urls import url

from core import views

urlpatterns = [
	url(r'^$', views.HomeView, name='home'),
	url(r'^lancamento/$', views.LancamentoView, name='lancamento'),
]