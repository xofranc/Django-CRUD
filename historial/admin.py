from django.contrib import admin
from .models import Paciente, Doctor

# Register your models here.


class DoctorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'especialidad', 'hospital_actual')
    filter_horizontal = ('pacientes_asignados', )

class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'gender', 'telefono')
    

admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Doctor, DoctorAdmin)
