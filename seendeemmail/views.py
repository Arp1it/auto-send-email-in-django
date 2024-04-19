from django.shortcuts import render, HttpResponse, redirect
from . models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .task import *

from django.contrib.auth import get_user_model

User = get_user_model()


# Create your views here.
@login_required(login_url="/loginn")
def main(request):
    fetcher = MailSender.objects.filter(cuser=request.user)

    return render(request, "index.html", context={"fetcher":fetcher})

@login_required(login_url="/loginn")
def storing(request):
    if request.method == "POST":
        titl = request.POST["titleofe"]
        mmsg = request.POST['yourmsg']
        recemail = request.POST['receiveremail']
        sendD = request.POST["sendingdate"]

        msgsender = MailSender.objects.create(cuser=request.user, title=titl, msg=mmsg, receiveremail=recemail, sendingdate=sendD)
        msgsender.save()

        # send_mail_task.delay()

        return redirect("/")

@login_required(login_url="/loginn")
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
            try:
                user = User.objects.create_user(username=uname, email=email, password=passsword)
                user.save()

                userr = authenticate(username=uname, email=email, password=passsword)

                if userr is not None:
                    login(request, userr)
                    return redirect("/")
                
            except Exception as e:
                print(e)
                return redirect("/")

        else:
            return redirect("/")

    return render(request, "sigin.html")

def loginn(request):
    if request.method == "POST":
        loginusername = request.POST['username']
        uemail = request.POST["email"]
        uspasw = request.POST["pasw"]

        userr = authenticate(username=loginusername, email=uemail, password=uspasw)

        if userr is not None:
            login(request, userr)
            return redirect("/")

        return redirect("/loginn")
        
    return render(request, "login.html")


@login_required(login_url="/loginn")
def loggout(request):
    if request.user:
        logout(request)
        return redirect("/loginn")

    else:
        return redirect("/sigin")


# def e(request):
#     # sleepy.delay(30)
#     send_mail_task.delay()
#     return HttpResponse("hELLEO,")