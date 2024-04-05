from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  
    path('proveedor_list/', views.proveedor_list, name='proveedor_list'),
    path('proveedor_create/', views.proveedor_create, name='proveedor_create'),
    path('producto_list/', views.producto_list, name='producto_list'),
    path('producto_create/', views.producto_create, name='producto_create'),
]

