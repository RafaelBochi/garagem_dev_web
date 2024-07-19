from rest_framework.viewsets import ModelViewSet
from core.models.imagem import ImagemVeiculo
from core.serializers import ImagemVeiculoSerializer

class ImagemVeiculoViewSet(ModelViewSet):
    queryset = ImagemVeiculo.objects.all()
    serializer_class = ImagemVeiculoSerializer