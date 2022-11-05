from dataclasses import fields
from django import forms
from django.forms import ModelForm
from .models import *
import dateutil.parser

class reservaForm(ModelForm, forms.Form):
    maximo = '15/11/2022'
    dt= dateutil.parser
    maximo1 = dt.parse(maximo).date()


    fecha= forms.DateField(widget=forms.DateInput(attrs={'type': 'date','min': datetime.now().date, 'max': maximo1}))
        
    class Meta:
            
        model =Reserva 
        fields = ['id_reserva', 'fecha' ,'servicio','hora','cuenta']

        

 
