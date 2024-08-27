from django.forms import ModelForm
from .models import Paciente, Persona


class PacienteForm(ModelForm):
    class Meta:
        model = Paciente
        fields = ['nombre', 'apellido', 'gender', 'direccion', 'telefono', 'email']




