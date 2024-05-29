from rest_framework import permissions, viewsets
from apps.registro_hora_extra.models import RegistroHoraExtra
from .serializers import RegistroHoraExtraSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class BancoHorasViewSet(viewsets.ModelViewSet):
    queryset = RegistroHoraExtra.objects.all()
    serializer_class = RegistroHoraExtraSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]
