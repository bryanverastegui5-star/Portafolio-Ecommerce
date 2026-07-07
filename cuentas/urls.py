from django.urls import path

from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [

    path(
        "login/",
        LoginView.as_view(
            template_name="cuentas/login.html"
        ),
        name="login"
    ),

    path(
        "registro/",
        views.registro,
        name="registro"
    ),

    path(
        "logout/",
        views.cerrar_sesion,
        name="logout"
    ),

    path(
        "perfil/",
        views.perfil,
        name="perfil"
    ),

    path(
        "mis-pedidos/",
        views.mis_pedidos,
        name="mis_pedidos"
    ),

    path(
        "pedido/<int:pedido_id>/",
        views.detalle_pedido,
        name="detalle_pedido"
    ),

]