from django.urls import path, include
from . import views

# from .task import *
# from django.confs.urls.defaults import *

urlpatterns = [
    path("",  views.main, name='home'),
    path("storing",  views.storing, name='sstor'),
    path("del/<int:sl>",  views.dele, name='delete'),
    path("sigin",  views.sigin, name='sigin'),
    path("loginn",  views.loginn, name='loginn'),
    path("loggout",  views.loggout, name='loggout'),
    path("passupdate",  views.passupdate, name='passupdate'),
    # path("e",  views.e, name='e'),
]