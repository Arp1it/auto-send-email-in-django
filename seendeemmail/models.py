from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


# Create your models here.
class MailSender(models.Model):
    cuser = models.ForeignKey(User, on_delete=models.CASCADE, related_name="mailuser")
    title = models.CharField(max_length=100, default="You not given title of message.")
    msg = models.CharField(max_length=99999)
    receiveremail = models.EmailField(max_length=50)
    sendingdate = models.CharField(default=str(now), max_length=30)
    timestamp = models.DateTimeField(default=now)