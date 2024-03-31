from celery import shared_task
from time import sleep
from django.core.mail import send_mail
from .models import *
import datetime


@shared_task
def sleepy(duration):
    sleep(duration)
    return None


@shared_task
def send_mail_task(bind=True):
    b = MailSender.objects.all()
    a = datetime.datetime.now()

    if len(b) > 0:
        for bs in b:
            if f"{a.date()}T{a.strftime('%H:%M')}" >= bs.sendingdate:
                send_mail(bs.title, bs.msg,
                        "arpitrraa@gmail.com",
                        [bs.receiveremail],
                        fail_silently=False)
                MailSender.objects.filter(id=bs.id).delete()
                
        return None