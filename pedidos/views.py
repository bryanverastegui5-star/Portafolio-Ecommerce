from decimal import Decimal

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from .models import Pedido, DetallePedido
from productos.models import Producto


@login_required
def finalizar_compra(request):

    carrito = request.session.get("carrito", {})

    if not carrito:

        messages.warning(
            request,
            "Tu carrito está vacío."
        )

        return redirect("ver_carrito")

    total = Decimal("0")

    pedido = Pedido.objects.create(

        usuario=request.user,

        total=0

    )

    for producto_id, item in carrito.items():

        producto = Producto.objects.get(id=producto_id)

        subtotal = Decimal(str(item["precio"])) * item["cantidad"]

        DetallePedido.objects.create(

            pedido=pedido,

            producto=producto,

            cantidad=item["cantidad"],

            precio=item["precio"],

            subtotal=subtotal,

        )

        total += subtotal

    pedido.total = total

    pedido.save()

    request.session["carrito"] = {}

    messages.success(

        request,

        "¡Compra realizada correctamente!"

    )

    return redirect("catalogo")