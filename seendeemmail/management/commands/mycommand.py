from django.core.management.base import BaseCommand

from seendeemmail.task import send_mail_task
# from django.core.mail import send_mail

from seendeemmail.models import *
import datetime
from termcolor import colored

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from django.contrib.auth import get_user_model

User = get_user_model()


class Command(BaseCommand):
    help = 'Runs my function continuously'

    def handle(self, *args, **options):
        while True:
            try:
                b = MailSender.objects.all()
                a = datetime.datetime.now()
                u = User.objects.all()


                if len(b) > 0:
                    for bs in b:
                        if f"{a.date()}T{a.strftime('%H:%M')}" >= bs.sendingdate:

                            send_mail_task.delay(from_email=bs.cuser.email, emaillist=bs.receiveremail, subject=bs.title, message=bs.msg, aut_user=bs.cuser.email, aut_password=bs.cuser.user_email_password)

                            MailSender.objects.filter(id=bs.id).delete()

                            # Notify frontend via Channels about the deletion
                            channel_layer = get_channel_layer()
                            async_to_sync(channel_layer.group_send)(
                                "frontend_updates", {"type": "data_deleted", "data": bs.id, "message":"Successfully send the message"}
                            )

            except KeyboardInterrupt:
                print(colored("KeyboardInterrupt", "red"))
                return None
            
# run this file by python manage.py mycommand