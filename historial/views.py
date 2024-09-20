from django.shortcuts import render, redirect, get_list_or_404

from .form import PacienteForm, CustomUserCreationForm
from .models import Paciente, Doctor
from .form import PacienteForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import IntegrityError
# from django.http import HttpResponse


# Create your views here.


# login
def entry(request):
    if request.method == 'GET':
        return render(request, 'login.html', {
            'form': AuthenticationForm()
        })
    else:
        # Autenticar al usuario
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is None:
            # Si la autenticación falla, mostrar un mensaje de error
            return render(request, 'login.html', {
                'form': AuthenticationForm(),
                'error': 'Username or password is incorrect'
            })
        else:
            # Si la autenticación es exitosa, loguear al usuario y redirigir
            login(request, user)
            return redirect('about')



# registro de usuarios en la pagina web
def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': CustomUserCreationForm()  # Usa el formulario personalizado
        })
    else:
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()  # Guarda al usuario con los datos validados
                login(request, user)  # Loguea al usuario
                return redirect('home')  # Redirige al usuario después del registro
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': form,
                    'error': "El nombre de usuario ya existe"
                })
        else:
            return render(request, 'signup.html', {
                'form': form,
                'error': "Por favor corrige los errores a continuación"
            })

# vistas de la pagina web
def home(request):
    return render(request, 'home.html')

# about page
def about(request):
    return render(request, 'about.html')



# funciones que requieren estar loggeado en la pagina web para actualizar o modificar valores

# vista de las historias clinicas ya creadas
@login_required
def pacientes(request):
    Paciente.objects.all()

    return render(request, 'database.html', {
        'paciente': Paciente.objects.filter(dataComplete=True)
    })



# creacion de nuevas historrias clinicas
@login_required
def crear_paciente(request):
    if request.method == 'GET':
        return render(request, 'crear_paciente.html', {
            'form': PacienteForm
        })
    else:
        form = PacienteForm(request.POST)
        new_historia = form.save(commit=False)
        print(new_historia)
        return render(request, 'crear_paciente.html', {
            'form': PacienteForm
        })


# salida de sesion del usuario
@login_required
def out(request):
    logout(request)
    return redirect('home')

@login_required
def complete(request, historialId):
    paciente = get_list_or_404(Paciente, id= historialId, user=request.user)
    if request.method == 'POST':
        Paciente.delete()
        return redirect('home')
    
    
@login_required
def deleteHistory(request, historialId):
    paciente = get_list_or_404(Paciente, id=historialId, user=request.user)
    if request.method == 'POST':
        paciente.delete()
        return redirect('home')


@login_required
def detail(request, historialId):
    if request.method == 'GET':
        pass

@login_required
def crear_Paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            form = PacienteForm()
            return render(request, 'crear_paciente.html', {
                'form': form
            })

@login_required
def lista_Pacientes(request):
    pass


