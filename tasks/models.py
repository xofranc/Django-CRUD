from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# creacion de Usuarios


class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    fechaNacimiento = models.DateField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    

class History(models.Model):
    pass

    def __str__(self):
        return self.title + ' - By ' + self.user.username
    