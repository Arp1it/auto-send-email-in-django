from celery import shared_task
from time import sleep
from django.core.mail import send_mail
from .models import *
# import datetime

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


@shared_task
def sleepy(duration):
    sleep(duration)
    return None


# @shared_task
# def send_mail_task():
#     b = MailSender.objects.all()
#     a = datetime.datetime.now()

#     if len(b) > 0:
#         for bs in b:
#             if f"{a.date()}T{a.strftime('%H:%M')}" >= bs.sendingdate:
#                 send_mail(bs.title, bs.msg,
#                         "arpitrraa@gmail.com",
#                         [bs.receiveremail],
#                         fail_silently=False)
#                 MailSender.objects.filter(id=bs.id).delete()
                
#         return None
    

@shared_task
def send_mail_task(emaillist, from_email, subject, message, aut_user, aut_password):
    def sendMail(fromEmail, toEmail, subject, message, auth_user, auth_password):
        msg = MIMEMultipart()
        # msg.set_unixfrom("arpit")
        msg['From'] = fromEmail
        msg['To'] = toEmail
        msg['Subject'] = subject
        msg.attach(MIMEText(message))
        mailserver = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        mailserver.ehlo()
        mailserver.login(auth_user, auth_password)
        mailserver.sendmail(fromEmail, toEmail, msg.as_string())
        mailserver.quit()

    emaillist = emaillist.split(",")
    print(emaillist)

    for emai in emaillist:
        fromEmail = from_email
        toEmail = emai

        try:
            sendMail(fromEmail, toEmail, subject, message, aut_user, aut_password)
            print(f'Mail sent to {emai}')

        except Exception as e:
            print(e)
            # channel_layer = get_channel_layer()
            # async_to_sync(channel_layer.group_send)(
            #     "frontend_updates", {"type": "error_send", "message":f"{emai} not exists"}
            # )

    return None


# running celery file by this command - celery -A seendeeemailoauto worker -l info -P eventlet