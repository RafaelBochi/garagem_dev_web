from rest_framework.serializers import ModelSerializer
from core.models.imagem import ImagemVeiculo

class ImagemVeiculoSerializer(ModelSerializer):
    class Meta:
        model = ImagemVeiculo
        fields = "__all__"