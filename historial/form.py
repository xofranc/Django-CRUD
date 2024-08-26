from django.forms import ModelForm
from .models import Paciente


class PacienteForm(ModelForm):
    class Meta:
        model = Paciente
        fields = ['nombre', 'apellido', 'fecha_nacimiento', 'sexo', 'direccion', 'telefono']