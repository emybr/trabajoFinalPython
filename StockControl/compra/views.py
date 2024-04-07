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

from django.shortcuts import render
from django.http import HttpResponse
from .models import Proveedor

def proveedor_create(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        dni = request.POST.get('dni')

        if dni and int(dni) < 0:
            error_message = "El DNI no puede ser un número negativo."
            return render(request, 'proveedor_create.html', {'error_message': error_message, 'nombre': nombre, 'apellido': apellido, 'dni': dni})
        
        if len(nombre) > 50 or len(apellido) > 50:
            error_message = "El nombre y el apellido no deben superar los 50 caracteres cada uno."
            return render(request, 'proveedor_create.html', {'error_message': error_message, 'nombre': nombre, 'apellido': apellido, 'dni': dni})
        
        if nombre and apellido and dni:
            try:
                dni = int(dni)
            except ValueError:
                error_message = "El DNI debe ser un número válido."
                return render(request, 'proveedor_create.html', {'error_message': error_message, 'nombre': nombre, 'apellido': apellido, 'dni': dni})
            proveedor = Proveedor.objects.create(
                nombre=nombre,
                apellido=apellido,
                dni=dni
            )
            return render(request, 'proveedor_create.html', {'proveedor': proveedor})
        else:
            error_message = "Por favor, complete todos los campos."
            return render(request, 'proveedor_create.html', {'error_message': error_message, 'nombre': nombre, 'apellido': apellido, 'dni': dni})
    
    return render(request, 'proveedor_create.html')




def producto_list(request):
    productos = Producto.objects.all()
    return render(request, 'productos_list.html', {'productos': productos})


from django.shortcuts import render, get_object_or_404
from .models import Producto, Proveedor

from django.shortcuts import render, get_object_or_404
from .models import Producto, Proveedor

def producto_create(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        precio = request.POST.get('precio')
        stock = request.POST.get('stock')
        proveedor_id = request.POST.get('proveedor')

        nombre_guardado = nombre
        precio_guardado = precio
        stock_guardado = stock
        proveedor_id_guardado = proveedor_id
        
        if nombre and precio and stock and proveedor_id:
            try:
                precio = precio.replace(',', '.')  
                precio = float(precio)
                if precio <= 0:
                    raise ValueError
            except ValueError:
                error_message = "El precio debe ser un número válido y mayor que cero."
                proveedores = Proveedor.objects.all()
                return render(request, 'producto_create.html', {'error_message': error_message, 'nombre': nombre_guardado, 'precio': precio_guardado, 'stock': stock_guardado, 'proveedor_id': proveedor_id_guardado, 'proveedores': proveedores})
            
            try:
                stock = int(stock)
                if stock < 0:
                    raise ValueError
            except ValueError:
                error_message = "El stock debe ser un número válido y mayor o igual que cero."
                proveedores = Proveedor.objects.all()
                return render(request, 'producto_create.html', {'error_message': error_message, 'nombre': nombre_guardado, 'precio': precio_guardado, 'stock': stock_guardado, 'proveedor_id': proveedor_id_guardado, 'proveedores': proveedores})
            
            if len(nombre) > 50:
                error_message = "El nombre no puede exceder los 50 caracteres."
                proveedores = Proveedor.objects.all()
                return render(request, 'producto_create.html', {'error_message': error_message, 'nombre': nombre_guardado, 'precio': precio_guardado, 'stock': stock_guardado, 'proveedor_id': proveedor_id_guardado, 'proveedores': proveedores})
            
            proveedor = get_object_or_404(Proveedor, id=proveedor_id)
            
            producto = Producto.objects.create(
                nombre=nombre,
                precio=precio,
                stock=stock,
                proveedor=proveedor
            )
            return render(request, 'producto_create.html', {'producto': producto})
        else:
            error_message = "Por favor, complete todos los campos."
            proveedores = Proveedor.objects.all()
            return render(request, 'producto_create.html', {'error_message': error_message, 'nombre': nombre_guardado, 'precio': precio_guardado, 'stock': stock_guardado, 'proveedor_id': proveedor_id_guardado, 'proveedores': proveedores})
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
        nombre = request.POST.get('nombre')
        precio = request.POST.get('precio')
        stock = request.POST.get('stock')
        proveedor_id = request.POST.get('proveedor')
        
        
        if len(nombre) > 50:
            error_message = "El nombre no debe superar los 50 caracteres."
            return render(request, 'producto_editar.html', {'error_message': error_message, 'producto': producto, 'proveedores': proveedores})
        
        if precio and float(precio) <= 0:
            error_message = "El precio debe ser mayor que cero."
            return render(request, 'producto_editar.html', {'error_message': error_message, 'producto': producto, 'proveedores': proveedores})
        

        if stock and int(stock) < 0:
            error_message = "El stock no puede ser negativo."
            return render(request, 'producto_editar.html', {'error_message': error_message, 'producto': producto, 'proveedores': proveedores})
        
        if nombre and precio and stock and proveedor_id:
            try:
                precio = float(precio)
                stock = int(stock)
            except ValueError:
                error_message = "El precio y el stock deben ser números válidos."
                return render(request, 'producto_editar.html', {'error_message': error_message, 'producto': producto, 'proveedores': proveedores})
            
            proveedor = get_object_or_404(Proveedor, id=proveedor_id)
            producto.nombre = nombre
            producto.precio = precio
            producto.stock = stock
            producto.proveedor = proveedor
            producto.save()
            
            return HttpResponseRedirect(reverse('producto_list'))
        else:
            error_message = "Por favor, complete todos los campos."
            return render(request, 'producto_editar.html', {'error_message': error_message, 'producto': producto, 'proveedores': proveedores})
    return render(request, 'producto_editar.html', {'producto': producto, 'proveedores': proveedores})



def proveedor_eliminar(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        proveedor.delete()
        return HttpResponseRedirect(reverse('proveedor_list'))
    return render(request, 'proveedor_eliminar.html', {'proveedor': proveedor})

import re

def proveedor_editar(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        dni = request.POST.get('dni')
        
        
        if len(nombre) > 50 or len(apellido) > 50:
            error_message = "El nombre y el apellido no deben superar los 50 caracteres cada uno."
            return render(request, 'proveedor_editar.html', {'error_message': error_message, 'proveedor': proveedor})
        

        if not re.match("^[0-9]+$", dni):
            error_message = "El DNI debe contener solo números."
            return render(request, 'proveedor_editar.html', {'error_message': error_message, 'proveedor': proveedor})
        

        if dni and int(dni) < 0:
            error_message = "El DNI no puede ser un número negativo."
            return render(request, 'proveedor_editar.html', {'error_message': error_message, 'proveedor': proveedor})
        
        if nombre and apellido and dni:
            proveedor.nombre = nombre
            proveedor.apellido = apellido
            proveedor.dni = dni
            proveedor.save()
            return HttpResponseRedirect(reverse('proveedor_list'))
        else:
            error_message = "Por favor, complete todos los campos."
            return render(request, 'proveedor_editar.html', {'error_message': error_message, 'proveedor': proveedor})
    
    return render(request, 'proveedor_editar.html', {'proveedor': proveedor})






