from django.urls import path
from .views import *


urlpatterns = [
    path('index', index, name="index"),
    path('login', login, name="login"),
    path('registro', registro, name="registro"),
    
    ]