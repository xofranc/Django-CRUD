from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import TaskForm
from .models import Task
from django.utils import timezone
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request, 'home.html')


# Tareas
@login_required
def tasks(request):
    Task.objects.all()

    return render(request, 'tasks.html', {
        'tasks': Task.objects.filter(user=request.user, dateCompleted__isnull=True)
    })


@login_required
def taskCompleted(request):
    Task.objects.all()

    return render(request, 'tasks.html', {
        'tasks': Task.objects.filter(user=request.user, dateCompleted__isnull=False).order_by('-dateCompleted')
    })


@login_required
def createTask(request):
    # si es igual a un metodo GET, devolvera el formulario
    if request.method == "GET":
        return render(request, 'create_task.html', {
            'form': TaskForm
        })

    # agrega los datos obtenidos del formulario a la base de datos de la lista de tareas
    else:
        try:
            form = TaskForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'create_task.html', {
                'form': TaskForm,
                'errorMessage': 'Please provide a valid form.'
            })


@login_required
def taskDetails(request, taskId):
    if request.method == "GET":
        task = get_object_or_404(Task, id=taskId, user=request.user)
        form = TaskForm(instance=task)
        return render(request, 'task_detail.html', {
            'task': task,
            'form': form
        })
    else:
        try:
            task = get_object_or_404(Task, id=taskId, user=request.user)
            form = TaskForm(request.POST, instance=task)
            form.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'task_detail.html', {
                'task': task,
                'form': form,
                'errorMessage': 'Error updating Task'
            })


@login_required
def completeTask(request, taskId):
    task = get_object_or_404(Task, id=taskId, user=request.user)
    if request.method == 'POST':
        task.dateCompleted = timezone.now()
        task.save()
        return redirect('tasks')


@login_required
def deleteTask(request, taskId):
    task = get_object_or_404(Task, id=taskId, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks')


# Inicio de Sesion y creacion de usuarios
@login_required
def signout(request):
    logout(request)
    return redirect('home')


def entry(request):
    if request.method == "GET":
        return render(request, 'login.html', {
            'form': AuthenticationForm
        })
    else:
        # Obtiene los datos del usuario ya registrado
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'login.html', {
                'form': AuthenticationForm,
                'error': "username or password is incorrect"
            })
        else:
            login(request, user)
            return redirect('tasks')


def signIn(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:

            try:
                # registrar Usuario
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('tasks')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': "username ya existe"
                })

        return render(request, 'signup.html', {
            'form': UserCreationForm,
            'error': "passwords No coinciden"
        })
