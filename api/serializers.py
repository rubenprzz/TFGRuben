from rest_framework import serializers
from .models import Estudiante


class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = ('id', 'nombre', 'apellidos', 'fecha_nacimiento', 'asignaturas', 'created_at')
