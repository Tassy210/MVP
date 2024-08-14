from django.test import TestCase

# Create your tests here.
from django.core import mail
from django.test import TestCase
from .emails import enviar_email_html

class EmailTests(TestCase):
    def test_email_send(self):
        destinatarios = ['lanalarala@gmail.com']
        assunto = 'Teste Automatizado'
        contexto = {
            'variavel1': 'valor1',
            'variavel2': 'valor2',
        }

        enviar_email_html(destinatarios, assunto, contexto)

        self.assertEqual(len(mail.outbox), 1)
        email = mail.outbox[0]
        self.assertEqual(email.subject, assunto)
        self.assertIn('valor1', email.body)
        self.assertIn('<p>Este é um e-mail de exemplo', email.alternatives[0][0])
