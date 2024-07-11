from django.contrib.auth.models import User
from django.db import models


class Asignatura(models.Model):
    nombre = models.CharField(max_length=100)
    profesor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='asignaturas')
    horario = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Estudiante(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    email = models.EmailField()
    fecha_nacimiento = models.DateField()
    asignaturas = models.ManyToManyField(Asignatura, through='Inscripcion')

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"


class Profesor(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    email = models.EmailField()
    fecha_nacimiento = models.DateField()
    fecha_ingreso = models.DateField()

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"


class Inscripcion(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    fecha_inscripcion = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.estudiante} en {self.asignatura}"


class Asistencia(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    fecha = models.DateField()
    estado = models.CharField(max_length=10,
                              choices=[('Presente', 'Presente'), ('Ausente', 'Ausente'), ('Retraso', 'Retraso')])

    class Meta:
        unique_together = ('estudiante', 'asignatura', 'fecha')
