from django.shortcuts import render, redirect, get_object_or_404

from .models import *
from .forms import *
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
#region Inicio

def home(request):
    return render(request, 'home.html') 
def medico(request):
    return render(request, 'medico.html') 
def auxiliar(request):
    return render(request, 'auxiliar.html') 
def persona(request):
    return render(request, 'persona.html') 

login_required

# crear_usuario
def crear_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_usuarios')
    else:
        form = UsuarioForm()

    return render(request, 'usuario/crear_usuario.html', {'form': form})

# listar_usuarios
def listar_usuarios(request):
    usuarios = Usuario.objects.all()  # Obtiene todos los usuarios
    return render(request, 'usuario/listar_usuarios.html', {'usuarios': usuarios})

# eliminar usuario
def eliminar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    usuario.delete()  # Elimina el usuario directamente
    return redirect('listar_usuarios')

# actualizar usuario
def actualizar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)

    if request.method == 'POST':
        form = UsuarioUpdateForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('listar_usuarios')  # O donde necesites
    else:
        form = UsuarioUpdateForm(instance=usuario)

    return render(request, 'usuario/actualizar_usuario.html', {'form': form})

# region login
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # Redirección según puesto_empresa
            if user.puesto_empresa == "it":
                return redirect("home")
            elif user.puesto_empresa == "medico":
                return redirect("medico")
            elif user.puesto_empresa == "persona":
                return redirect("persona")
            elif user.puesto_empresa == "auxiliar":
                return redirect("auxiliar")
            else:
                return redirect("home")  # Redirección por defecto

        else:
            return render(request, "auth/login.html", {"error": "Credenciales inválidas"})

    return render(request, "auth/login.html")

# crear persona
def crear_persona(request):
    if request.method =='POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_personas')
    else:
        form = PersonaForm()
    return render(request, 'persona/crear_persona.html', {'form':form})

# listar persona
def listar_personas(request):
    persona = Persona.objects.filter(is_active=True)
    return render(request, 'persona/listar_personas.html', {'persona_list':persona})

# reactivar usuarios
def reactivar_persona(request, id):
    persona = get_object_or_404(Persona, id=id)
    persona.is_active = True
    persona.save()
    return redirect('listar_personas')

# eliminar persona
def desactivar_persona(request, persona_id):
    persona = get_object_or_404(Persona, id=persona_id)
    persona.is_active = False
    persona.save()
    return redirect('listar_personas_inactivas')

# listar personas inactivas
def listar_personas_inactivas(request):
    personas_inactivas = Persona.objects.filter(is_active=False)
    return render(request, 'persona/listar_personas_inactivas.html', {'personas_inactivas': personas_inactivas})


# actualizar persona
def actualizar_persona(request, persona_id):
    persona = get_object_or_404(Persona, id=persona_id)

    if request.method == 'POST':
        form = PersonaForm(request.POST, instance=persona)
        if form.is_valid():
            form.save()
            return redirect('listar_personas')  # Redirige a la lista después de actualizar
    else:
        form = PersonaForm(instance=persona)

    return render(request, 'persona/actualizar_persona.html', {'form': form})

#region eps

# crear eps
def crear_eps(request):
    if request.method =='POST':
        form = EpsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_eps')
    else:
        form = EpsForm()
    return render(request, 'eps/crear_eps.html', {'form':form})

# listar eps
def listar_eps(request):
    eps = Eps.objects.all()
    return render(request, 'eps/listar_eps.html',{'listar_eps':eps})

# actualizar eps
def actualizar_eps(request, eps_id):
    eps = get_object_or_404(Eps, id=eps_id)

    if request.method == 'POST':
        form = EpsForm(request.POST, instance=eps)
        if form.is_valid():
            form.save()
            return redirect('listar_eps')  # Redirige a la lista de EPS después de actualizar
    else:
        form = EpsForm(instance=eps)

    return render(request, 'eps/actualizar_eps.html', {'form': form})

# eliminar eps
def eliminar_eps(request, eps_id):
    eps = get_object_or_404(Eps, id=eps_id)
    eps.delete()
    return redirect('listar_eps')


# region Contrato

# crear_contrato
def crear_contrato(request):
    if request.method == 'POST':
        form = ContratoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_contratos')  # Redirige a la lista de contratos después de crear
    else:
        form = ContratoForm()

    return render(request, 'contrato/crear_contrato.html', {'form': form})


# listar_contrato
def listar_contratos(request):
    contratos = Contrato.objects.all()  # Obtenemos todos los registros de Contratos
    return render(request, 'contrato/listar_contratos.html', {'listar_contratos': contratos})


# actualizar_contrato
def actualizar_contrato(request, contrato_id):
    contrato = get_object_or_404(Contrato, id=contrato_id)

    if request.method == 'POST':
        form = ContratoForm(request.POST, instance=contrato)
        if form.is_valid():
            form.save()
            return redirect('listar_contratos')  # Redirige a la lista de contratos después de actualizar
    else:
        form = ContratoForm(instance=contrato)

    return render(request, 'contrato/actualizar_contrato.html', {'form': form})

# eliminar contrata
def eliminar_contrato(request, contrato_id):
    contrato = get_object_or_404(Contrato, id=contrato_id)
    contrato.delete()
    return redirect('listar_contratos')

# region Formacion

# crear
def crear_formacion(request):
    if request.method == 'POST':
        form = FormacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_formaciones')  # Redirige a la lista de formaciones después de crear
    else:
        form = FormacionForm()

    return render(request, 'formacion/crear_formacion.html', {'form': form})

# listar
def listar_formaciones(request):
    formaciones = Formacion.objects.all()  # Obtenemos todos los registros de Formaciones
    return render(request, 'formacion/listar_formaciones.html', {'listar_formaciones': formaciones})

# actuaizar
def actualizar_formacion(request, formacion_id):
    formacion = get_object_or_404(Formacion, id=formacion_id)

    if request.method == 'POST':
        form = FormacionForm(request.POST, instance=formacion)
        if form.is_valid():
            form.save()
            return redirect('listar_formacion')  # Redirige a la lista de formaciones después de actualizar
    else:
        form = FormacionForm(instance=formacion)

    return render(request, 'formacion/actualizar_formacion.html', {'form': form})

# eliminar formacion
def eliminar_formacion(request, formacion_id):
    formacion = get_object_or_404(Formacion, id=formacion_id)
    formacion.delete()
    return redirect('listar_formaciones')
#region empleado

def crear_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_empleados')
    else:
        form = EmpleadoForm()
    return render(request, 'empleado/crear_empleado.html', {'form': form})

def listar_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'empleado/listar_empleados.html', {'empleados': empleados})

def actualizar_empleado(request, empleado_id):
    empleado = get_object_or_404(Empleado, id=empleado_id)
    if request.method == 'POST':
        form = EmpleadoForm(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
            return redirect('listar_empleados')
    else:
        form = EmpleadoForm(instance=empleado)
    return render(request, 'empleado/actualizar_empleado.html', {'form': form})

def eliminar_empleado(request, empleado_id):
    empleado = get_object_or_404(Empleado, id=empleado_id)
    empleado.delete()
    return redirect('listar_empleados')



# region Usuario







# region Salas


