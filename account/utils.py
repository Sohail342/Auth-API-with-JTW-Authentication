from django.core.mail import EmailMessage
import os

class Util:
    @staticmethod
    def send_mail(data):
        email = EmailMessage(
            subject=data['email_subject'],
            body=data['body'],
            from_email=os.environ.get('EMAIL_FROM'),
            to=[data['to_mail']]
        )
        email.send()