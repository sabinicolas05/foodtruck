from rest_framework.serializers import ModelSerializer
from apps.productos.models import Productos

class ProducSerializer(ModelSerializer):
    class Meta:
        model = Productos
        fields = '__all__'