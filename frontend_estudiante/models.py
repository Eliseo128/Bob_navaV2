from django.db import models

# Create your models here.
class Estudiante(models.Model):
    num_estudiante = models.PositiveIntegerField()
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    area_estudio = models.CharField(max_length=50)
    gpa = models.FloatField()

    def __str__(self):
        return f" Estudiante: {self.nombre} {self.apellido} ({self.email})"