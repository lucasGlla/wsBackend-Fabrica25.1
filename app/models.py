from django.db import models

class UsuarioModel(models.Model):
    nomeUsuario = models.CharField(max_length=255)
    emailUsuario = models.CharField(max_length=255)

    def __str__(self):
        return self.nomeUsuario


class AvatarModel(models.Model):
    usuario = models.ForeignKey(UsuarioModel,on_delete=models.CASCADE,related_name="Avatares")
    avatarUrl = models.URLField()

    def __str__(self):
        return f"avatar de {self.usuario.nomeUsuario}"

# Create your models here