from django.shortcuts import render
from Servicios.models import Servicios

# Create your views here.

def home(request):
    return render(request, "ProyectoWebApp/home.html")



