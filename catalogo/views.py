from rest_framework import viewsets

from .models import Filme, Genero
from .serializers import FilmeSerializer, GeneroSerializer


class GeneroViewSet(viewsets.ModelViewSet):
    queryset = Genero.objects.all().order_by('id')
    serializer_class = GeneroSerializer


class FilmeViewSet(viewsets.ModelViewSet):
    queryset = Filme.objects.select_related('genero').order_by('id')
    serializer_class = FilmeSerializer
