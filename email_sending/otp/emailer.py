from django.core.mail import send_mail
from django.conf import settings

def sendOtpToEmail(email , subject , message):
    send_mail(subject , message, settings.EMAIL_HOST_USER , [email])