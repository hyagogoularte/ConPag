from django.test import TestCase

# Create your tests here.
class TestarChamadas(TestCase):

    def teste_chamada_home_view_sem_logar(self):
        response = self.client.get('/home/', follow=True)
        self.assertRedirects(response, '/login/')

        response = self.client.post('/home/', follow=True)
        self.assertRedirects(response, '/login/')

