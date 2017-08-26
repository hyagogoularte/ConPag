from django.test import TestCase
from django.core.urlresolvers import reverse
from django.test import Client

# Create your tests here.
class TestarChamadas(TestCase):
    def setUp(self):
        self.client = Client()

    def teste_chamada_lancamentos_view_sem_logar(self):
        response = self.client.get('/lancamentos/', follow=True)
        self.assertRedirects(response, '/?next=/lancamentos/')

    def teste_chamada_novo_lancamentos_view_sem_logar(self):
        response = self.client.get(reverse('novo-lancamento'), follow=True)
        self.assertRedirects(response, '/?next=/lancamentos/novo/')


class TestarTemplates(TestCase):
    def setUp(self):
        self.client = Client()

    def teste_chamada_lancamento_view_logando(self):
        self.client.login(username='gerson', password='qwer1234')
        response = self.client.get(reverse('home'), follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
