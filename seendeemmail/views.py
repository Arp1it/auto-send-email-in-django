from django.shortcuts import render, HttpResponse


# Create your views here.
def main(requests):
    return render(requests, "index.html")


def fetching(requests):
    pass