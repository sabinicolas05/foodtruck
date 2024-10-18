from rest_framework.viewsets import ModelViewSet
from apps.productos.models import Productos
from apps.productos.api.serializers import ProducSerializer

class ProductosModelViewSet(ModelViewSet):
    serializer_class= ProducSerializer
    queryset = Productos.objects.all()