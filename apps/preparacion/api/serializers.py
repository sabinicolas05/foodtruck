from rest_framework.serializers import ModelSerializer
from apps.preparacion.models import ZonaPreparacion

class zonaPreparacionSerializer(ModelSerializer):
    class Meta:
        model = ZonaPreparacion
        fields = '__all__'