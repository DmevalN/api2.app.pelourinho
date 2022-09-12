from rest_framework.serializers import ModelSerializer
from administrador.models import Usuario

class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('nome','email', 'pais', 'estado', 'cidade', 'telefone', 'ativo')