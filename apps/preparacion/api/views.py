from rest_framework.viewsets import ModelViewSet
from apps.preparacion.models import ZonaPreparacion
from apps.preparacion.api.serializers import zonaPreparacionSerializer

class zonaPreparacionModelViewSet(ModelViewSet):
    serializer_class= zonaPreparacionSerializer
    queryset = ZonaPreparacion.objects.all()