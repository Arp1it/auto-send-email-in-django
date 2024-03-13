from django.shortcuts import render, HttpResponse, redirect
from . models import *
from django.contrib.auth.models import User


# Create your views here.
def main(request):
    fetcher = MailSender.objects.all()

    return render(request, "index.html", context={"fetcher":fetcher})

def storing(request):
    if request.method == "POST":
        titl = request.POST["titleofe"]
        mmsg = request.POST['yourmsg']
        recemail = request.POST['receiveremail']
        sendD = request.POST["sendingdate"]

        print(mmsg, recemail, sendD)

        msgsender = MailSender.objects.create(cuser=request.user, msg=mmsg, receiveremail=recemail, sendingdate=sendD)
        msgsender.save()

        return redirect("/")
    
def dele(request, sl):
    delet = MailSender.objects.filter(id=sl).delete()

    return redirect("/")

def sigin(request):
    if request.method == "POST":
        uname = request.POST["name"]
        email = request.POST["email"]
        passsword = request.POST["passs1"]
        cpassword = request.POST["passs2"]

        if passsword == cpassword:
            user = User.objects.create_user(username=uname, email=email, password=passsword)

        else:
            return redirect("/")

    return render(request, "sigin.html")

def loginn(request):
    return render(request, "login.html")