from django.db import models

# Create your models here.


class Productos(models.Model):
    nombre = models.CharField(max_length=100)
    presentacion = models.CharField(max_length=30)
    fecha_creacion = models.DateTimeField()
    cantidad= models.IntegerField()

    def __str__(self):
        return self.nombre

class Cambio_stock(models.Model):
    INGRESO = 'Ingreso'
    EGRESO = 'Egreso'
    TIPO_CAMBIO_CHOICES = [
        (INGRESO, 'Ingreso'),
        (EGRESO, 'Egreso'),
    ]
    ref_id = models.ForeignKey(Productos,on_delete=models.CASCADE)
    cantidad= models.IntegerField()
    comentario= models.CharField(max_length=100)
    fecha = models.DateTimeField()
    tipo_cambio = models.CharField(max_length=7, choices=TIPO_CAMBIO_CHOICES)
    def __str__(self):
        return self.ref_id.nombre