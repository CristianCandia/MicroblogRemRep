from flask_mail import Message
from decorators import async
from app import mail


def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender = sender, recipients = recipients)
    msg.body = text_body
    msg.html = html_body
    print 'Enviando mensaje a ' + str(recipients)
    mail.send(msg)
    print 'Mensaje enviado'