from django.shortcuts import render, HttpResponse, redirect
from . models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .task import *
from django.contrib import messages

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

        return redirect("/")

@login_required(login_url="/loginn")
def dele(request, sl):
    delet = MailSender.objects.filter(id=sl).delete()

    return redirect("/")


def authenticator(request, username, email, password, path):
    userr = authenticate(username=username, email=email, password=password)

    print(path)

    if userr is not None:
        login(request, userr)
        if path == "/loginn":
            messages.success(request, "Successfully logged in!")
        elif path == "/sigin":
            messages.success(request, "Successfully signed in!")
    
    else:
        if path == "/loginn":
            messages.error(request, "Login failed. Please try again.")
            # return redirect(f"/{path}")
        elif path == "/sigin":
            messages.error(request, "Sigin failed. Please try again.")
            # return redirect(f"/{path}")


def sigin(request):
    if request.user.is_authenticated:
        return redirect("/")
    
    else:
        if request.method == "POST":
            uname = request.POST["name"]
            email = request.POST["email"]
            passsword = request.POST["passs1"]
            cpassword = request.POST["passs2"]
            empass = request.POST["passs3"]

            if passsword == cpassword:
                try:
                    user = User.objects.create_user(username=uname, email=email, password=passsword, user_email_password=empass)
                    user.save()

                    path = request.path
                    authenticator(request, username=uname, email=email, password=passsword, path=path)

                    return redirect("/sigin")
                    
                except Exception as e:
                    print(e)
                    messages.error(request, "Sigin failed. Please try again.")
                    return redirect("/sigin")

            else:
                return redirect("/sigin")

        return render(request, "sigin.html")

def loginn(request):
    if request.user.is_authenticated:
        return redirect("/")
    
    else:
        if request.method == "POST":
            loginusername = request.POST['username']
            uemail = request.POST["email"]
            uspasw = request.POST["pasw"]

            path = request.path
            authenticator(request, username=loginusername, email=uemail, password=uspasw, path=path)

            return redirect("/loginn")
            
        return render(request, "login.html")


@login_required(login_url="/loginn")
def loggout(request):
    if request.user:
        logout(request)
        return redirect("/loginn")

    else:
        return redirect("/sigin")
    

@login_required(login_url="/loginn")
def passupdate(request):
    return render(request, "passupdate.html")


# def e(request):
#     # sleepy.delay(30)
#     send_mail_task.delay()
#     return HttpResponse("hELLEO,")