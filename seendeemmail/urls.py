from django.urls import path, include
from . import views

urlpatterns = [
    path("",  views.main, name='home'),
    path("storing",  views.storing, name='sstor'),
]