from django.shortcuts import redirect,get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from datetime import datetime
from .forms import ProductoForm
from .models import Productos

# Create your views here.

# Vista principal de Productos
def productosIndex(request):
    # Consultar productos
    productos = Productos.objects.all()
    #Obtener el template
    template = loader.get_template("productos.html")
    #Agregar el contexto
    context = {"productos":productos}

    # Renderizar el template con el contexto
    rendered_template = template.render(context, request)

    # Retornar respuesta HTTP
    return HttpResponse(rendered_template)


# Vista para crear productos
def sumarProducto(request):
    #Obtener el template
    template = loader.get_template("sumarProducto.html")
    #Generar Formulario
    if request.method == "POST":
        form = ProductoForm(request.POST or None, request.FILES)
        if form.is_valid():
            #obtener datos del formulario
            producto_nuevo = form.save(commit=False)
            cantidad = form.cleaned_data.get('cantidad')

            # Establecer tipo_cambio como "Ingreso"
            producto_nuevo.tipo_cambio = 'Ingreso'

            #Asignar fecha de creación
            producto_nuevo.fecha_creacion = datetime.now()
            producto_nuevo.fecha = datetime.now()
            
            producto = producto_nuevo.ref_id
            producto.cantidad += cantidad
            #Guardar Producto
            producto.save()
            producto_nuevo.save()
            return redirect('productosIndex')
    else:
        form = ProductoForm()
    #Crear contexto
    context = {}
    context['form'] = form
    #Retornar respuesta http
    return HttpResponse(template.render(context,request))

    
def restarProducto(request):
    # Obtener el template
    template = loader.get_template("restarProducto.html")
    
    # Generar Formulario
    if request.method == "POST":
        form = ProductoForm(request.POST or None, request.FILES)
        if form.is_valid():
            # Obtener datos del formulario
            producto_nuevo = form.save(commit=False)
            cantidad = form.cleaned_data.get('cantidad')

            # Validar que la cantidad a restar no exceda la cantidad actual del producto
            if cantidad <= producto_nuevo.ref_id.cantidad:
                # Establecer tipo_cambio como "Egreso"
                producto_nuevo.tipo_cambio = 'Egreso'
                # Asignar fecha de creación y fecha actual
                producto_nuevo.fecha_creacion = datetime.now()
                producto_nuevo.fecha = datetime.now()
                # Actualizar la cantidad del producto
                producto = producto_nuevo.ref_id
                producto.cantidad -= cantidad
                producto.save()
                # Guardar el producto
                producto_nuevo.save()
                return redirect('productosIndex')
            else:
                # Si la cantidad a restar es mayor que la cantidad actual del producto, mostrar un mensaje de error
                context = {'form': form, 'error_message': 'La cantidad a restar es mayor que la cantidad actual del producto.'}
                return HttpResponse(template.render(context, request))
    else:
        form = ProductoForm()
    # Crear contexto
    context = {'form': form}
    # Retornar respuesta http
    return HttpResponse(template.render(context, request))