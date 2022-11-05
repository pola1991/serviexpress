from django.shortcuts import render, redirect
from django.db.models import Q
from core.forms import * 
from .models import *   

# Create your views here.

def index(request):
    return render(request, 'core/index.html')


def crear_r(request):

    datos = {
        'form' : reservaForm()
    }
    if request.method == 'POST':
        formulario = reservaForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = 'Guardado exitosamente'

    return render(request,'core/reservar/read.html', datos)


def read_r(request):
    reserva = Reserva.objects.all()

    datos = {
       
        'reserva': reserva
        
    }
    return render(request,'core/reservar/read_r.html', datos)

    

def eliminar_r(request,id):
    reserva = Reserva.objects.get(id_reserva = id)
    reserva.delete()
    return redirect(to = 'read_r')