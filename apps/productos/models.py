from django.db import models

class Productos(models.Model):
    nombre_del_producto = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio_del_producto = models.DecimalField(max_digits=10, decimal_places=5)
     

    def __str__(self):
        return self.nombre_del_producto
