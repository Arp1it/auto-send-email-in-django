from django.shortcuts import render, HttpResponse, redirect
from . models import *


# Create your views here.
def main(requests):
    return render(requests, "index.html")


def fetching(requests):
    pass


def storing(requests):
    if requests.method == "POST":
        mmsg = requests.POST['yourmsg']
        recemail = requests.POST['receiveremail']

        print(mmsg, recemail)

        return redirect("/")