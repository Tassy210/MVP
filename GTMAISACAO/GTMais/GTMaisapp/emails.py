from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def enviar_email_html(destinatarios, assunto, contexto):
    html_message = render_to_string('emails/email_template.html', contexto)
    plain_message = strip_tags(html_message)

    email = EmailMessage(
        subject=assunto,
        body=plain_message,
        from_email='liraoharak@gmail.com',
        to=destinatarios,
        headers={'Reply-To': 'liraoharak@gmail.com'}
    )
    email.content_subtype = "html"  # Main content is now text/html
    email.send()
