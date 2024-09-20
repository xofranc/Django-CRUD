from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from datetime import date

# Create your models here.

# Modelo general para paciente y doctores
class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='M')
    email = models.EmailField(unique=True)
    direccion = models.CharField(max_length=120, null=False)


    class Meta:
        abstract = True

    # Paciente
class Paciente(Persona):
    historial_medico = models.TextField(default="No se ha registrado historial médico.")
    fecha_nacimiento = models.DateField(default=date(2000, 1, 1))
    direccion = models.CharField(max_length=255)  # Dirección del paciente
    telefono = models.IntegerField(null=False)
    dataComplete = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Doctor(Persona):
    especialidad = models.CharField(max_length=100)  # Especialidad del doctor
    numero_licencia = models.CharField(max_length=20, default="1234567")  # Número de licencia médica
    anios_experiencia = models.PositiveIntegerField(default=0)  # Años de experiencia
    hospital_actual = models.CharField(max_length=150, default= 'None')  # Hospital donde trabaja actualmente
    telefono_contacto = models.CharField(max_length=10, default = '3214567890')  # Número de contacto
    horario_atencion = models.CharField(max_length=100, default="08:00-17:00")
    consulta_online = models.BooleanField(default=False)  # Si ofrece consultas en línea
    fecha_registro = models.DateTimeField(default=timezone.now)  # Fecha de registro
    pacientes_asignados = models.ManyToManyField(Paciente, related_name='doctores_asignados')  # Relación de pacientes asignados
    user = models.ForeignKey(User, on_delete=models.CASCADE, default = None)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.especialidad}"