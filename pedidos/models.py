from django.db import models
from django.contrib.auth.models import User

from productos.models import Producto


class Pedido(models.Model):

    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    fecha = models.DateTimeField(
        auto_now_add=True
    )

    total = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    ESTADOS = [

        ("Pendiente", "Pendiente"),

        ("Pagado", "Pagado"),

        ("Enviado", "Enviado"),

        ("Entregado", "Entregado"),

    ]

    estado = models.CharField(

        max_length=20,

        choices=ESTADOS,

        default="Pendiente"

    )

    def __str__(self):

        return f"Pedido #{self.id} - {self.usuario.username}"


class DetallePedido(models.Model):

    pedido = models.ForeignKey(

        Pedido,

        on_delete=models.CASCADE,

        related_name="detalles"

    )

    producto = models.ForeignKey(

        Producto,

        on_delete=models.CASCADE

    )

    cantidad = models.PositiveIntegerField()

    precio = models.DecimalField(

        max_digits=10,

        decimal_places=2

    )

    subtotal = models.DecimalField(

        max_digits=10,

        decimal_places=2

    )

    def __str__(self):

        return self.producto.nombre