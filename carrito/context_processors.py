def carrito(request):

    carrito = request.session.get("carrito", {})

    cantidad = 0

    total = 0

    for item in carrito.values():

        cantidad += item["cantidad"]

        total += item["precio"] * item["cantidad"]

    return {

        "cantidad_carrito": cantidad,

        "total_carrito": total,

    }