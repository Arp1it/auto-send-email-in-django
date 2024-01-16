from django.shortcuts import render, HttpResponse, redirect
from . models import *


# Create your views here.
def main(requests):
    return render(requests, "index.html")


def fetching(requests):
    pass


def storing(request):
    if request.method == "POST":
        mmsg = request.POST['yourmsg']
        recemail = request.POST['receiveremail']
        sendD = request.POST["sendingdate"]

        print(mmsg, recemail, sendD)

        msgsender = MailSender.objects.create(cuser=request.user, msg=mmsg, receiveremail=recemail, sendingdate=sendD)
        msgsender.save()

        return redirect("/")