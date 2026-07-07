from django.shortcuts import render, redirect, get_object_or_404

from productos.models import Producto
from productos.forms import ProductoForm

from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User

from pedidos.models import Pedido
from django.db.models import Sum


def lista_mangas(request):

    mangas = Producto.objects.all()

    return render(
        request,
        "productos/admin/lista_mangas.html",
        {
            "mangas": mangas
        }
    )


def agregar_manga(request):

    if request.method == "POST":

        formulario = ProductoForm(request.POST, request.FILES)

        if formulario.is_valid():
            formulario.save()
            return redirect("lista_mangas")

    else:

        formulario = ProductoForm()

    return render(
        request,
        "productos/admin/formulario_manga.html",
        {
            "formulario": formulario
        }
    )


def editar_manga(request, pk):

    manga = get_object_or_404(Producto, pk=pk)

    if request.method == "POST":

        formulario = ProductoForm(
            request.POST,
            request.FILES,
            instance=manga
        )

        if formulario.is_valid():
            formulario.save()
            return redirect("lista_mangas")

    else:

        formulario = ProductoForm(instance=manga)

    return render(
        request,
        "productos/admin/formulario_manga.html",
        {
            "formulario": formulario
        }
    )


def eliminar_manga(request, pk):

    manga = get_object_or_404(Producto, pk=pk)

    if request.method == "POST":

        manga.delete()

        return redirect("lista_mangas")

    return render(
        request,
        "productos/admin/confirmar_eliminar.html",
        {
            "manga": manga
        }
    )

@staff_member_required
def dashboard(request):

    total_productos = Producto.objects.count()

    total_usuarios = User.objects.count()

    total_pedidos = Pedido.objects.count()

    ventas = Pedido.objects.aggregate(

        total=Sum("total")

    )

    total_ventas = ventas["total"] or 0

    return render(

        request,

        "productos/admin/dashboard.html",

        {

            "total_productos": total_productos,

            "total_usuarios": total_usuarios,

            "total_pedidos": total_pedidos,

            "total_ventas": total_ventas,

        },

    )
