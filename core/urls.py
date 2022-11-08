from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name="index"),
    path('login', login, name="login"),
    path('registro', registro, name="registro"),
    path('crear_r',crear_r,name='crear_r'),
    path('read_r', read_r ,name='read_r'),
    path('eliminar_r/<id>',eliminar_r,name='eliminar_r'),
    path('confirmada/<id>',confirmada,name='confirmada'),
    path('crear_s',crear_s,name='crear_s'),
    path('read_s',read_s,name='read_s'),
    path('registro/', registro, name="registro")
    ]