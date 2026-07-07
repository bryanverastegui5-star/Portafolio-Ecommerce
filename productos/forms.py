from django import forms
from .models import Producto


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto

        fields = [
            "categoria",
            "nombre",
            "descripcion",
            "precio",
            "stock",
            "imagen",
            "disponible",
        ]

        widgets = {
            "descripcion": forms.Textarea(
                attrs={"rows": 4}
            ),
        }