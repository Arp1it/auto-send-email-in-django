from django.urls import path, include
from . import views

urlpatterns = [
    path("",  views.main, name='home'),
    path("storing",  views.storing, name='sstor'),
    path("del/<int:sl>",  views.dele, name='delete'),
    path("sigin",  views.sigin, name='sigin'),
    path("loginn",  views.loginn, name='loginn'),
    path("e",  views.e, name='e'),
]