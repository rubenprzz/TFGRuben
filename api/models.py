from datetime import timezone, date

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Asignatura(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    profesor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='asignaturas')
    horario = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)  # Add this line

    def __str__(self):
        return self.nombre


class Estudiante(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    apellidos = models.CharField(max_length=50)
    email = models.EmailField()
    fecha_nacimiento = models.DateField()
    asignaturas = models.ManyToManyField(Asignatura, through='Inscripcion')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"

    @property
    def edad_actual(self):
        if self.fecha_nacimiento:
            today = date.today()
            age = today.year - self.fecha_nacimiento.year - (
                    (today.month, today.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day))
            return age

        return 0


class Profesor(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    apellidos = models.CharField(max_length=50)
    email = models.EmailField()
    fecha_nacimiento = models.DateField()
    fecha_ingreso = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"


class Inscripcion(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    fecha_inscripcion = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.estudiante} en {self.asignatura}"


class Asistencia(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    fecha = models.DateField()
    estado = models.CharField(max_length=10,
                              choices=[('Presente', 'Presente'), ('Ausente', 'Ausente'), ('Retraso', 'Retraso')])
    created_at = models.DateTimeField(default=timezone.now)  # Add this line

    class Meta:
        unique_together = ('estudiante', 'asignatura', 'fecha')
