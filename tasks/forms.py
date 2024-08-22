from django.forms import ModelForm
from .models import Persona

class TaskForm(ModelForm):
    class Meta:
        model = Persona
        fields = ['nombre', 'fecha de Nacimiento', 'creado']


class HistoryForm(ModelForm):
    pass