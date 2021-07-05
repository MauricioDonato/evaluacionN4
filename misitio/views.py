from django.shortcuts import render
from django.http import HttpResponse, response, HttpResponseRedirect
from django.shortcuts import render
from pasteleria.models import Cliente
from django.utils import timezone
from django.urls import reverse
import re
import sys
from itertools import cycle
# Create your views here.

def index(request):

    return render(request, 'pasteleria/index.html',)

def frm_registrar_cli(request):
 
   return render(request, 'pasteleria/frm_registrar_cli.html',)

def registrar_cliente(request):
    error = 'Error en el ingreso del'
    v_error = False
    primer_erro = False 
    rut_c = request.POST['rut']
    rut_c = rut_c.replace(' ','')
    rut_c = rut_c.replace('.','')
    rut_c = rut_c.replace('.','')
    rut_c = rut_c.replace('-','')
    
    nombre = request.POST['nombre']
    nombre = nombre.replace(' ','')
    apellido = request.POST['apellido'] 
    apellido = apellido.replace(' ','')
    fecha = request.POST['Fecha_nacimiento']  
   
    correo= request.POST['correo']    
    correo = correo.replace(' ','')
    contrasena= request.POST['contrasena'] 
    contrasena= nombre.replace(' ','')   
    validar_contrasena= request.POST['validar_contrasena']    
    cantidad = len(rut_c)

    if request.POST['contrasena'] != request.POST['validar_contrasena']:
        return HttpResponse('las contraseñas deben ser iguales')
    if(fecha =="" or apellido =="" or correo =="" or nombre =="" or contrasena =="" or rut_c ==""):
        return render(request, 'pasteleria/error_ingreso.html')
    if cantidad < 8:
        return render(request, 'pasteleria/error_ingreso.html')
    if cantidad > 10:
        return render(request, 'pasteleria/error_ingreso.html')
    aux = rut_c[:-1]
    dv = rut_c[-1:]
 
    revertido = map(int, reversed(str(aux)))
    factors = cycle(range(2,8))
    s = sum(d * f for d, f in zip(revertido,factors))
    res = (-s)%11
 
    if str(res) == dv:
        v_error = True
    elif dv=="K" and res==10:
        v_error = True
    else:
        v_error = False
    if v_error == False:
        return render(request,'pasteleria/error_rut.html')


    cliente = Cliente(rut=rut_c, nombre_cli=nombre, apellido_cli=apellido, fecha_nac=fecha, correo=correo, contrasena=contrasena, contrasena_val=validar_contrasena)
    cliente.save()
  
 
    return HttpResponseRedirect(reverse('pasteleria:cliente_regitrado'))
def cliente_regitrado(request):
    return render(request,'pasteleria/cliente_regitrado.html')

def frm_buscar_cliente(request):
    return render(request,'pasteleria/frm_buscar_cliente.html')
def buscar_y_mostrar_cliente(request):
    rut_b = request.POST['rut_b']
    listado =  Cliente.objects.filter(rut__startswith=rut_b)   
    
    carrito = {'listado':listado}
    return render(request, 'pasteleria/mostrar_cliente.html',carrito)
   
def eliminar_cliente(request):
    eliminador = Cliente.objects.get(id= request.POST['id_e'])
    eliminar_mostrar = {'eliminador':eliminador}
    return render(request, 'pasteleria/eliminar_cliente.html',eliminar_mostrar)
def eliminador_cliente(request):
    elim =  Cliente.objects.get(id= request.POST['id_eliminado'])
    elim.delete()
    return render(request, 'pasteleria/cliente_eliminado.html',)
def editar_cliente(request):
    editar =  Cliente.objects.get(id= request.POST['id_d'])
    editar_mostrar ={'editar': editar}
    return render(request, 'pasteleria/editar_cliente.html',editar_mostrar)
def editador_cliente(request):
    e = Cliente.objects.get(id= request.POST['id_editor'])
    rut_c = request.POST['rut_editor']
    rut_c = rut_c.replace(' ','')
    nombre = request.POST['nombre_editor']
    nombre = nombre.replace(' ','')
    apellido = request.POST['apellido_editor'] 
    apellido = apellido.replace(' ','')
    fecha = request.POST['Fecha_nacimiento_editor']  
    correo= request.POST['correo_editor']    
    correo = correo.replace(' ','')
    contrasena= request.POST['contrasena_editor'] 
    contrasena = contrasena.replace(' ','')   
    validar_contrasena= request.POST['validar_contrasena_editor']
    if request.POST['contrasena_editor'] != request.POST['validar_contrasena_editor']:
        return HttpResponse('las contraseñas deben ser iguales')
    if(fecha =="" or apellido =="" or correo =="" or nombre =="" or contrasena =="" or rut_c ==""):
        return render(request, 'pasteleria/error_ingreso.html')
    if len(request.POST['rut_editor']) < 8 and len(request.POST['rut_editar']) < 10:
        return render(request, 'pasteleria/error_ingreso.html')
    aux = rut_c[:-1]
    dv = rut_c[-1:]
 
    revertido = map(int, reversed(str(aux)))
    factors = cycle(range(2,8))
    s = sum(d * f for d, f in zip(revertido,factors))
    res = (-s)%11
 
    if str(res) == dv:
        v_error = True
    elif dv=="K" and res==10:
        v_error = True
    else:
        v_error = False
    if v_error == False:
        return render(request,'pasteleria/error_rut.html')

    e.rut = rut_c
    e.nombre_cli = nombre
    e.apellido_cli = apellido
    e.fecha_nac = fecha
    e.correo = correo
    e.contrasena = contrasena
    e.contrasena_val = validar_contrasena

    e.save()
    return render(request, 'pasteleria/editar_c.html',)   

  