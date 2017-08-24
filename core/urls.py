from django.conf.urls import url

from core import views

urlpatterns = [
	url(r'^$', views.HomeView, name='home'),
]