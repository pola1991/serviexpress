from django.shortcuts import render, redirect
from .forms import * 
from .models import *   
from django.contrib.auth import authenticate, login

# Create your views here.

def index(request):
    return render(request, 'core/index.html')


def login1(request):
    return render(request, 'core/registration/login1.html')


def registro1(request):
    return render(request, 'core/registration/registro1.html')

def crear_r(request):

    datos = {
        'form' : reservaForm()
    }
    if request.method == 'POST':
        formulario = reservaForm(request.POST)
        
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = 'Guardado exitosamente'

    return render(request,'core/reservar/crear_r.html', datos)


def read_r(request):
    reserva = Reserva.objects.all()

    datos = {
       
        'reserva': reserva
        
    }
    
    return render(request,'core/reservar/read_r.html', datos)

   
def confirmada(request, id):
    reserva = Reserva.objects.get(id_reserva = id)
    datos = {
        'form' : Reserva(instance= reserva)
    }
    if request.method == 'PUT':
        formulario = reservaForm(request.PUT, instance= reserva)
        datos1= reserva.confirmada == True
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Modificado exitosamente"
    
    return render(request,'core/reservar/read_r.html', datos, datos1) 


def eliminar_r(request,id):
    reserva = Reserva.objects.get(id_reserva = id)
    reserva.delete()
    return redirect(to = 'read_r')


def crear_s(request):

    datos = {
        'form' : servicioForm()
    }
    if request.method == 'POST':
        formulario = servicioForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = 'Guardado exitosamente'

    return render(request,'core/servicio/crear_s.html', datos)

def read_s(request):
    reserva = Reserva.objects.all()

    datos = {
       
        'reserva': reserva
        
    }
    return render(request,'core/servicio/read_s.html', datos)

    
def registro(request):
   
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            return redirect(to="index")
        else:
            data["form"] = formulario

    return render(request, 'registration/registro.html', data)

