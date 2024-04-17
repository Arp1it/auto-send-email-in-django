from django.core.management.base import BaseCommand
from seendeemmail.task import send_mail_task
from seendeemmail.models import *
import datetime
from django.core.mail import send_mail
from termcolor import colored

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


class Command(BaseCommand):
    help = 'Runs my function continuously'

    def handle(self, *args, **options):
        while True:
            try:
                # send_mail_task.delay()
                b = MailSender.objects.all()
                a = datetime.datetime.now()

                if len(b) > 0:
                    for bs in b:
                        if f"{a.date()}T{a.strftime('%H:%M')}" >= bs.sendingdate:
                            send_mail(bs.title, bs.msg,
                                    "your gamil",
                                    [bs.receiveremail],
                                    fail_silently=False)
                            MailSender.objects.filter(id=bs.id).delete()
                            # Notify frontend via Channels about the deletion
                            channel_layer = get_channel_layer()
                            async_to_sync(channel_layer.group_send)(
                                "frontend_updates", {"type": "data_deleted"}
                            )

            except KeyboardInterrupt:
                print(colored("KeyboardInterrupt", "red"))
                return None
            
# run this file by python manage.py mycommand