from django.forms import ModelForm
from django import forms
from .models import Paciente, Persona
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class PacienteForm(ModelForm):
    class Meta:
        model = Paciente
        fields = ['nombre', 'apellido', 'gender', 'direccion', 'telefono', 'email']



class LoginForms(ModelForm):
    username = forms.CharField(max_length=120, label='Usuario')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)  # Ejemplo de un campo adicional

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

