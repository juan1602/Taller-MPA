from django.urls import path

from . import views

urlpatterns = [
    #ruta, vista, nombre interno
    path('',views.productosIndex, name='productosIndex'),
    path('sumar/',views.sumarProducto, name='sumarProducto'),
    path('restar/',views.restarProducto, name='restarProducto'),

]