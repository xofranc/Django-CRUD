from django.db import models

# Create your models here.

# define las propiedades del paciente
class Paciente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    sexo = models.CharField(max_length=1, choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro no especificado')])
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)
    email = models.EmailField()

    def __str__(self):
        return f'{self.apellido}, {self.nombre}'