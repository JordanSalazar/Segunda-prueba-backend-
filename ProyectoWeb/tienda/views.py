from django.shortcuts import render
from .models import Producto, CategoriaProd

# Create your views here.

def tienda(request):
    productos = Producto.objects.all()
    return render(request, "tienda/tienda.html", {'productos': productos})


def categoria(request, categoria_id):
    categoria = CategoriaProd.objects.get(id = categoria_id)
    productos = Producto.objects.filter(categorias = categoria)
    return render(request, "tienda/categoria.html", {'categoria': categoria, 'productos': productos})
