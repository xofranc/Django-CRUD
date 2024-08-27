from django.contrib import admin
from .models import Paciente, Doctor

# Register your models here.

admin.site.register(Paciente)
admin.site.register(Doctor)