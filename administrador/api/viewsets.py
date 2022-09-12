from rest_framework.viewsets import ModelViewSet
from administrador.models import Usuario
from .serializers import UsuarioSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class UsuarioViewSet(ModelViewSet):
    #permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    """
    A simple ViewSet for viewing and editing accounts.
    """
    serializer_class = UsuarioSerializer

    def get_queryset(self):
        return Usuario.objects.all()
    