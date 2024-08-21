from django.test import TestCase
from django.core import mail
from .emails import enviar_email_html

class EmailTests(TestCase):
    def test_email_send(self):
        destinatarios = ['lanalarala@gmail.com']
        assunto = 'Teste Automatizado'
        contexto = {
         'Olá'
        }

        enviar_email_html(destinatarios, assunto, contexto)

        # Verifica se o e-mail foi enviado
        self.assertEqual(len(mail.outbox), 1)
        email = mail.outbox[0]
        self.assertEqual(email.subject, assunto)
        self.assertIn('Olá', email.body)
        
        # Verifica se o e-mail contém HTML
        self.assertTrue(email.alternatives)  # Verifica se há alternativas
        html_content = email.alternatives[0][0]
        self.assertIn('<p>Este é um e-mail de exemplo', html_content)

