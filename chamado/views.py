from chamado.models import Chamado
from chamado.serializers import ChamadoSerializer
from django.shortcuts import render
from rest_framework import viewsets

class ChamadoViewSet(viewsets.ModelViewSet):
    queryset = Chamado.objects.all()
    serializer_class = ChamadoSerializer