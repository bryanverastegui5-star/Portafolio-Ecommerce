from django.db import models

from django.contrib.auth.models import User

class Perfil(models.Model):

    usuario = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    telefono = models.CharField(
        max_length=20,
        blank=True
    )

    direccion = models.CharField(
        max_length=200,
        blank=True
    )

    ciudad = models.CharField(
        max_length=100,
        blank=True
    )

    region = models.CharField(
        max_length=100,
        blank=True
    )

    codigo_postal = models.CharField(
        max_length=20,
        blank=True
    )

    foto = models.ImageField(
        upload_to="perfiles/",
        blank=True,
        null=True
    )

    fecha_registro = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return self.usuario.username