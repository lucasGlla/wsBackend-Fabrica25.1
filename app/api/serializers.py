from rest_framework import serializers
from ..models import AvatarModel,UsuarioModel

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioModel
        fields = '__all__'

class AvatarSerializer(serializers.ModelSerializer):
    nomeUsuario = serializers.ReadOnlyField(source='usuario.nome')

    class Meta:
        model = AvatarModel
        fields = '__all__'