from rest_framework.serializers import ModelSerializer
from apps.pedidos.models import Pedido

class PediSerializer(ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'