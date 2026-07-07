from django.shortcuts import render, redirect

from productos.models import Producto


def ver_carrito(request):

    carrito = request.session.get("carrito", {})

    total = 0
    total_productos = 0

    for item in carrito.values():

        item["subtotal"] = item["precio"] * item["cantidad"]

        total += item["subtotal"]

        total_productos += item["cantidad"]

    return render(
        request,
        "carrito/carrito.html",
        {
            "carrito": carrito,
            "total": total,
            "total_productos": total_productos,
        },
    )


def agregar_carrito(request, producto_id):

    carrito = request.session.get("carrito", {})

    producto = Producto.objects.get(id=producto_id)

    if str(producto_id) in carrito:

        if carrito[str(producto_id)]["cantidad"] < producto.stock:

            carrito[str(producto_id)]["cantidad"] += 1

    else:

        carrito[str(producto_id)] = {

            "id": producto.id,

            "nombre": producto.nombre,

            "precio": float(producto.precio),

            "cantidad": 1,

            "imagen": producto.imagen.url if producto.imagen else "",

            "stock": producto.stock,

        }

    request.session["carrito"] = carrito

    return redirect("catalogo")


def eliminar_carrito(request, producto_id):

    carrito = request.session.get("carrito", {})

    carrito.pop(str(producto_id), None)

    request.session["carrito"] = carrito

    return redirect("ver_carrito")


def sumar_producto(request, producto_id):

    carrito = request.session.get("carrito", {})

    if str(producto_id) in carrito:

        producto = Producto.objects.get(id=producto_id)

        if carrito[str(producto_id)]["cantidad"] < producto.stock:

            carrito[str(producto_id)]["cantidad"] += 1

    request.session["carrito"] = carrito

    return redirect("ver_carrito")


def restar_producto(request, producto_id):

    carrito = request.session.get("carrito", {})

    if str(producto_id) in carrito:

        carrito[str(producto_id)]["cantidad"] -= 1

        if carrito[str(producto_id)]["cantidad"] <= 0:

            carrito.pop(str(producto_id))

    request.session["carrito"] = carrito

    return redirect("ver_carrito")