from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name="index"),
    path('crear_r',crear_r,name='crear_r'),
    path('read_r', read_r ,name='read_r'),
    path('eliminar_r/<id>',eliminar_r,name='eliminar_r'),

    ]