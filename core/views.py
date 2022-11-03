from django.shortcuts import render, redirect
from django.db.models import Q
# from core.forms import *  Debo hacer las tablas aun
# from .models import *    AUN NO ESTAN LOS MODELOS

# Create your views here.

def index(request):
    return render(request, 'core/index.html')