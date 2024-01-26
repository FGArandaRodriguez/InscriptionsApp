from django.db import models

# Create your models here.
class StudentInfo(models.Model):
    matricula = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    email = models.EmailField()
    fecha_inicio_ucamp = models.DateField(null=True, blank=True)
    fecha_baja_ucamp = models.DateField(null=True, blank=True)
    genero = models.CharField(max_length=10)
    moneda = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.matricula} - {self.nombre} {self.apellidos}"
