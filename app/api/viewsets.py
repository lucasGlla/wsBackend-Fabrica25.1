from rest_framework import viewsets
from rest_framework.response import Response
from app.models import UsuarioModel,AvatarModel
from .serializers import UsuarioSerializer,AvatarSerializer
import random

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = UsuarioModel.objects.all()
    serializer_class = UsuarioSerializer

class AvatarViewSet(viewsets.ModelViewSet):
    queryset = AvatarModel.objects.all()
    serializer_class = AvatarSerializer

    def create(self, request, *args, **kwargs):
        usuarioId = request.data.get("usuario")
        usuario = UsuarioModel.objects.get(id=usuarioId)
        nomeAleatorio = f"user{random.randint(1000,9999)}"
        avatarUrl = f"https://api.dicebear.com/9.x/adventurer/svg?seed={nomeAleatorio}"

        avatar = AvatarModel.objects.create(usuario=usuario,avatarUrl=avatarUrl)
        serializer = self.get_serializer(avatar)

        return Response(serializer.data)
    
    