from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

from .forms import RegistroUsuarioForm

from pedidos.models import Pedido


def registro(request):

    if request.method == "POST":

        formulario = RegistroUsuarioForm(request.POST)

        if formulario.is_valid():

            usuario = formulario.save()

            login(request, usuario)

            return redirect("catalogo")

    else:

        formulario = RegistroUsuarioForm()

    return render(
        request,
        "cuentas/registro.html",
        {
            "formulario": formulario
        }
    )


def cerrar_sesion(request):

    logout(request)

    return redirect("catalogo")


# ==========================================
# PERFIL
# ==========================================

@login_required
def perfil(request):

    return render(
        request,
        "cuentas/perfil.html"
    )


# ==========================================
# MIS PEDIDOS
# ==========================================

@login_required
def mis_pedidos(request):

    pedidos = Pedido.objects.filter(
        usuario=request.user
    ).order_by("-fecha")

    return render(
        request,
        "cuentas/mis_pedidos.html",
        {
            "pedidos": pedidos
        }
    )


# ==========================================
# DETALLE PEDIDO
# ==========================================

@login_required
def detalle_pedido(request, pedido_id):

    pedido = get_object_or_404(

        Pedido,

        id=pedido_id,

        usuario=request.user

    )

    return render(

        request,

        "cuentas/detalle_pedido.html",

        {

            "pedido": pedido

        }

    )