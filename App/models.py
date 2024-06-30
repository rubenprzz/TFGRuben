from pyclbr import Class

from django.contrib.auth.models import User
from django.db import models


class Subject(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subjects')
    schedule = models.CharField(max_length=100)


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    date_of_birth = models.DateField()
    subjects = models.ManyToManyField(Subject, through='Enrollment')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    date_of_birth = models.DateField()
    date_of_joining = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    date_enrolled = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student} en {self.subject}"


class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10,
                              choices=[('Presente', 'Presente'), ('Ausente', 'Ausente'), ('Retraso', 'Retraso')])

    class Meta:
        unique_together = ('student', 'subject', 'date')
