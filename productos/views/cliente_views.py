from django.shortcuts import render, get_object_or_404

from productos.models import Producto

def home(request):

    destacados = Producto.objects.filter(
        disponible=True
    ).order_by("-id")[:4]

    nuevos = Producto.objects.filter(
        disponible=True
    ).order_by("-id")[:8]

    recomendados = Producto.objects.filter(
        disponible=True
    ).order_by("?")[:4]

    return render(
        request,
        "productos/cliente/home.html",
        {
            "destacados": destacados,
            "nuevos": nuevos,
            "recomendados": recomendados,
        },
    )

from django.core.paginator import Paginator
from django.db.models import Q


def catalogo(request):

    mangas = Producto.objects.filter(disponible=True)

    # ==========================
    # BUSCADOR
    # ==========================

    busqueda = request.GET.get("buscar")

    if busqueda:

        mangas = mangas.filter(

            Q(nombre__icontains=busqueda) |

            Q(descripcion__icontains=busqueda)

        )

    # ==========================
    # ORDEN
    # ==========================

    orden = request.GET.get("orden")

    if orden == "precio":

        mangas = mangas.order_by("precio")

    elif orden == "-precio":

        mangas = mangas.order_by("-precio")

    elif orden == "nombre":

        mangas = mangas.order_by("nombre")

    else:

        mangas = mangas.order_by("-id")

    # ==========================
    # PAGINACIÓN
    # ==========================

    paginator = Paginator(mangas, 8)

    pagina = request.GET.get("page")

    mangas = paginator.get_page(pagina)

    return render(

        request,

        "productos/cliente/catalogo.html",

        {

            "mangas": mangas,

            "busqueda": busqueda,

            "orden": orden,

        },

    )

def detalle_manga(request, pk):

    manga = get_object_or_404(Producto, pk=pk)

    return render(
        request,
        "productos/cliente/detalle_manga.html",
        {
            "manga": manga
        }
    )


def buscar(request):

    return render(
        request,
        "productos/cliente/buscar.html"
    )


def categoria(request):

    return render(
        request,
        "productos/cliente/categoria.html"
    )