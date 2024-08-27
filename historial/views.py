from django.shortcuts import render, redirect, get_list_or_404

from .form import PacienteForm
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
            'form': AuthenticationForm
        })
    else:

        # obtiene los datos de los usuarios ya registrados

        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            return render(request, 'login.html', {
                'form': AuthenticationForm,
                'error': 'usarname or password is incorrect'
                })
        else:
            login(request, user)
            return redirect('about')



# registro de usuarios en la pagina web
def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:

            try:
                # registro Usuario
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': "username ya existe"
                })

        return render(request, 'signup.html', {
            'form': UserCreationForm,
            'error': "passwords No coinciden"
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
        'paciente': Paciente.objects.filter(user=request.user, dataComplete=True)
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

#
# def detailHistory(request, historialId):
#     if request.method == 'GET':
#         Paciente = get_list_or_404(Paciente, id=historialId, user=request.user)
#         form = PacienteForm(instance=paciente,)
#         return render(request, 'detailHistory.html', {
#             'form': form,
#             'paciente': paciente,
#             'error_message': 'Error creating history'
#             })
#     else:
#         try:
#             paciente = get_list_or_404(Paciente, id=historialId, user=request.user)
#             form = PacienteForm(request.POST, instance=paciente)
#             form.save()
#         except ValueError:
#             return render(request, 'detailHistory.html', {
#                 'form': form,
#                 'paciente': paciente,
#                 'error_message': 'Error creating history'
#             })

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