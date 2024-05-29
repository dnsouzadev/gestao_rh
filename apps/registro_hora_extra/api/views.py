from rest_framework import permissions, viewsets
from apps.registro_hora_extra.models import RegistroHoraExtra
from .serializers import RegistroHoraExtraSerializer


class BancoHorasViewSet(viewsets.ModelViewSet):
    queryset = RegistroHoraExtra.objects.all()
    serializer_class = RegistroHoraExtraSerializer
    permission_classes = [permissions.IsAuthenticated]
