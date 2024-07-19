from django.shortcuts import render
from rest_framework import generics

from api.models import Estudiante
from api.serializers import EstudianteSerializer


class EstudianteView(generics.CreateAPIView):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer
