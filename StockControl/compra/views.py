from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Proveedor, Producto
from django.urls import reverse

def index(request):
    return render(request, 'index.html')

def proveedor_list(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'proveedor_list.html', {'proveedores': proveedores})

def proveedor_create(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        dni = request.POST.get('dni')
        if nombre and apellido and dni:  
            proveedor = Proveedor.objects.create(
                nombre=nombre,
                apellido=apellido,
                dni=dni
            )
            return render(request, 'proveedor_create.html', {'proveedor': proveedor})
        else:
            error_message = "Por favor, complete todos los campos."
            return render(request, 'proveedor_create.html', {'error_message': error_message})
    return render(request, 'proveedor_create.html')

def producto_list(request):
    productos = Producto.objects.all()
    return render(request, 'productos_list.html', {'productos': productos})


def producto_create(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        precio = request.POST.get('precio')
        stock = request.POST.get('stock')
        proveedor_id = request.POST.get('proveedor')
        if nombre and precio and stock and proveedor_id:
            proveedor = Proveedor.objects.get(id=proveedor_id)
            producto = Producto.objects.create(
                nombre=nombre,
                precio=precio,
                stock=stock,
                proveedor=proveedor
            )
            return render(request, 'producto_create.html', {'producto': producto})
        else:
            error_message = "Por favor, complete todos los campos."
            return render(request, 'producto_create.html', {'error_message': error_message})
    else:
        proveedores = Proveedor.objects.all()
        return render(request, 'producto_create.html', {'proveedores': proveedores})
    
def producto_eliminar(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        if 'eliminar' in request.POST:  
            producto.delete()
            return HttpResponseRedirect(reverse('producto_list'))
        elif 'editar' in request.POST: 
            return HttpResponseRedirect(reverse('producto_editar', kwargs={'pk': pk}))
    return render(request, 'producto_eliminar.html', {'producto': producto})

def producto_editar(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    proveedores = Proveedor.objects.all()  
    if request.method == 'POST':
        producto.nombre = request.POST.get('nombre')
        producto.precio = request.POST.get('precio')
        producto.stock = request.POST.get('stock')
        proveedor_id = request.POST.get('proveedor')
        producto.proveedor = Proveedor.objects.get(id=proveedor_id)  
        producto.save()
        return HttpResponseRedirect(reverse('producto_list'))
    return render(request, 'producto_editar.html', {'producto': producto, 'proveedores': proveedores})


def proveedor_eliminar(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        proveedor.delete()
        return HttpResponseRedirect(reverse('proveedor_list'))
    return render(request, 'proveedor_eliminar.html', {'proveedor': proveedor})

def proveedor_editar(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        proveedor.nombre = request.POST.get('nombre')
        proveedor.apellido = request.POST.get('apellido')
        proveedor.dni = request.POST.get('dni')
        proveedor.save()
        return HttpResponseRedirect(reverse('proveedor_list'))
    return render(request, 'proveedor_editar.html', {'proveedor': proveedor})