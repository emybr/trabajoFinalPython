# from django.shortcuts import render
# from .models import Proveedor, Producto

# def produc(request):
#     return render(request, 'producs.html')

# def proveedor_list(request):
#     proveedores = Proveedor.objects.all()
#     return render(request, 'proveedor_list.html', {'proveedores': proveedores})

# def proveedor_create(request):
#     if request.method == 'POST':
#         nombre = request.POST.get('nombre')
#         apellido = request.POST.get('apellido')
#         dni = request.POST.get('dni')
#         proveedor = Proveedor.objects.create(
#             nombre=nombre,
#             apellido=apellido,
#             dni=dni
#         )
#         return render(request, 'proveedor_create.html', {'proveedor': proveedor})
#     return render(request, 'proveedor_create.html')


# def producto_list(request):
#     produc = Producto.objects.all()
#     return render(request, 'producs_list.html', {'produc': produc})
    

from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Proveedor, Producto

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
        if nombre and apellido and dni:  # Verifica si los campos no están vacíos
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

# def producto_create(request):
#     if request.method == 'POST':
#         nombre = request.POST.get('nombre')
#         precio = request.POST.get('precio')
#         stock = request.POST.get('stock')
#         proveedor = request.POST.get('proveedor')
#         if nombre and precio and stock and proveedor:  # Verifica si los campos no están vacíos
#             producto = Producto.objects.create(
#                 nombre=nombre,
#                 precio=precio,
#                 stock=stock,
#                 proveedor=proveedor
#             )
#             return render(request, 'producto_create.html', {'produc': producto})
#         else:
#             error_message = "Por favor, complete todos los campos."
#             return render(request, 'producto_create.html', {'error_message': error_message})
#     return render(request, 'producto_create.html')

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