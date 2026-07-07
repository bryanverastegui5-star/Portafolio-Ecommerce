from django.urls import path

from . import views

from productos.views.admin_views import dashboard

from productos.views.cliente_views import (
    home,
    catalogo,
    detalle_manga,
    buscar,
    categoria,
)

urlpatterns = [

    # -----------------------------
    # HOME
    # -----------------------------

    path(
        "",
        home,
        name="home"
    ),

    # -----------------------------
    # CATÁLOGO
    # -----------------------------

    path(
        "catalogo/",
        catalogo,
        name="catalogo"
    ),

    path(
        "detalle/<int:pk>/",
        detalle_manga,
        name="detalle_manga"
    ),

    path(
        "buscar/",
        buscar,
        name="buscar"
    ),

    path(
        "categoria/",
        categoria,
        name="categoria"
    ),

    # -----------------------------
    # ADMINISTRACIÓN
    # -----------------------------

    path(
        "administracion/productos/",
        views.lista_mangas,
        name="lista_mangas"
    ),

    path(
        "administracion/productos/nuevo/",
        views.agregar_manga,
        name="agregar_manga"
    ),

    path(
        "administracion/productos/editar/<int:pk>/",
        views.editar_manga,
        name="editar_manga"
    ),

    path(
        "administracion/productos/eliminar/<int:pk>/",
        views.eliminar_manga,
        name="eliminar_manga"
    ),
    path(
        "dashboard/",
        dashboard,
        name="dashboard"
    ),

]