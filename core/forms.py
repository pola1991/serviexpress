from dataclasses import fields
from django import forms
from django.forms import ModelForm
from .models import *
import dateutil.parser #PARA CAMBIAR FORMATO FECHA
from django.contrib.auth.forms import UserCreationForm

class reservaForm(ModelForm, forms.Form):
    maximo = '15/11/2022'
    dt= dateutil.parser
    maximo1 = dt.parse(maximo).date()


    fecha= forms.DateField(widget=forms.DateInput(attrs={'type': 'date','min': datetime.now().date, 'max': maximo1}))
        
    class Meta:
            
        model =Reserva
        fields = ['fecha' ,'servicio','hora']


class servicioForm(ModelForm):

        class Meta:
            
            model =Servicio
            fields = ['nombre_servicio','tipo','precio']


class CustomUserCreationForm(UserCreationForm):
    user = User.username
    if User.username == "gerente1":
        class Meta:
            model = User
            fields = ["username", "first_name", "last_name", "email","password1", "password2"]
    else:
        class Meta:
            model = User
            fields = ["username", "first_name", "last_name", "email","is_staff","password1", "password2"]

