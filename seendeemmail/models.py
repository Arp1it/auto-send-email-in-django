from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.conf import settings


from django.contrib.auth.models import AbstractUser
from .manager import UserManager


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    REQUIRED_FIELDS = []
    objects = UserManager()



from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
class MailSender(models.Model):
    cuser = models.ForeignKey(User, on_delete=models.CASCADE, related_name="mailuser")
    title = models.CharField(max_length=100)
    msg = models.CharField(max_length=99999)
    receiveremail = models.EmailField(max_length=50)
    sendingdate = models.CharField(max_length=30)
    timestamp = models.DateTimeField(default=now)