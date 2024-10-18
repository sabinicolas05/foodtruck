from django.db import models
from apps.pedidos.models import Pedido
from apps.productos.models import Producto
from apps.pedidos.models import Pedido

# Create your models here.
class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, related_name='detalles', on_delete=models.SET_NULL, null=True)
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)
    cantidad = models.PositiveIntegerField()
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.cantidad} - {self.producto.nombre_del_producto}"