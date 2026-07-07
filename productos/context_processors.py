from productos.models import Categoria


def categorias_globales(request):
    """
    Envía todas las categorías disponibles a todas las plantillas.
    """

    categorias = Categoria.objects.all().order_by("nombre")

    return {
        "categorias_menu": categorias
    }