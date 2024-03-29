from celery import shared_task
from time import sleep
from django.core.mail import send_mail


@shared_task
def sleepy(duration):
    sleep(duration)
    return None


@shared_task
def send_mail_task():
    send_mail("Celery Worked Yeah", 'Celery is cool',
              "from",
              ['to'],
              fail_silently=False)
    return None