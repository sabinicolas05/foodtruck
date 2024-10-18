from rest_framework.viewsets import ModelViewSet
from apps.pedidos.models import Pedido
from apps.pedidos.api.serializers import PediSerializer

class PedidoModelViewset(ModelViewSet):
    serializer_class= PediSerializer
    queryset = Pedido.objects.all()