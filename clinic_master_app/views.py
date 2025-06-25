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
                return redirect("persona")
            elif user.puesto_empresa == "persona":
                return redirect("persona")
            elif user.puesto_empresa == "auxiliar":
                return redirect("home")
            else:
                return redirect("persona") # Redirección por defecto
            
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
        form = ContratoForm(request.POST, request.FILES)  # No olvidar request.FILES
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
@login_required
def crear_formacion(request):
    persona = request.user.persona  # Paso 1
    empleado = get_object_or_404(Empleado, id_persona=persona)  # Paso 2

    if request.method == 'POST':
        form = FormacionForm(request.POST)
        if form.is_valid():
            formacion = form.save(commit=False)
            formacion.id_empleado = empleado  # Paso 3: asociar
            formacion.save()
            return redirect('listar_formaciones')
    else:
        form = FormacionForm()

    return render(request, 'formacion/crear_formacion.html', {'form': form})
# listar
@login_required
def listar_formaciones(request):
    persona = request.user.persona
    empleado = get_object_or_404(Empleado, id_persona=persona)
    formaciones = Formacion.objects.filter(id_empleado=empleado)
    return render(request, 'formacion/listar_formaciones.html', {'listar_formaciones': formaciones})

# actuaizar
@login_required
def actualizar_formacion(request, formacion_id):
    persona = request.user.persona
    empleado = get_object_or_404(Empleado, id_persona=persona)
    formacion = get_object_or_404(Formacion, id=formacion_id, id_empleado=empleado)

    if request.method == 'POST':
        form = FormacionForm(request.POST, instance=formacion)
        if form.is_valid():
            form.save()
            return redirect('listar_formaciones')
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

# ///////nuevo

# region crear documento empleado
# crear_documento_empleado
@login_required
def crear_documento_empleado(request):
    try:
        persona = request.user.persona
        empleado = Empleado.objects.get(id_persona=persona)
    except (AttributeError, Empleado.DoesNotExist):
        return render(request, 'error.html', {'mensaje': 'No tienes un perfil de empleado registrado.'})

    if request.method == 'POST':
        form = DocumentoEmpleadoForm(request.POST, request.FILES)
        if form.is_valid():
            documento = form.save(commit=False)
            documento.id_empleado = empleado  # Asociar al empleado logueado
            documento.save()
            return redirect('listar_documentos_empleado')
    else:
        form = DocumentoEmpleadoForm()  # ✅ Nada de inicial ni hidden

    return render(request, 'documento_empleado/crear_documento_empleado.html', {'form': form})
# listar_documentos_empleado
@login_required
def listar_documentos_empleado(request):
    try:
        persona = request.user.persona
        empleado = Empleado.objects.get(id_persona=persona)
        documentos = DocumentosEmpleado.objects.filter(id_empleado=empleado)
    except (AttributeError, Empleado.DoesNotExist):
        documentos = []  # o podrías mostrar un error

    return render(request, 'documento_empleado/listar_documentos_empleado.html', {'documentos': documentos})
# eliminar_documento_empleado
def eliminar_documento_empleado(request, documento_id):
    documento = get_object_or_404(DocumentosEmpleado, pk=documento_id)
    documento.delete()
    return redirect('listar_documentos_empleado')

# region movimiento
# crear_movimiento
def crear_movimiento(request):
    if request.method == 'POST':
        form = HistorialMovimientoForm(request.POST)  # <-- aquí usas el formulario, no el modelo
        if form.is_valid():
            form.save()
            return redirect('listar_movimientos')
    else:
        form = HistorialMovimientoForm()
    return render(request, 'historial_movimiento/crear_historial_movimiento.html', {'form': form})


# listar_movimientos
def listar_movimientos(request):
    movimientos = HistorialMovimientos.objects.all()
    return render(request, 'historial_movimiento/listar_movimientos.html', {'movimientos': movimientos})

# region realacion jerarquica
# crear_relacion_jerarquica
def crear_relacion_jerarquica(request):
    if request.method == 'POST':
        form = RelacionJerarquicaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_relaciones_jerarquicas')
    else:
        form = RelacionJerarquicaForm()
    return render(request, 'relacion_jerarquica/crear_relacion_jerarquica.html', {'form': form})

# listar_relaciones_jerarquicas
def listar_relaciones_jerarquicas(request):
    relaciones = RelacionesJerarquicas.objects.all()
    return render(request, 'relacion_jerarquica/listar_relaciones.html', {'relaciones': relaciones})

# eliminar_relacion_jerarquica
def eliminar_relacion_jerarquica(request, relacion_id):
    relacion = get_object_or_404(RelacionesJerarquicas, id=relacion_id)
    relacion.delete()
    return redirect('listar_relaciones_jerarquicas')

def editar_relacion_jerarquica(request, pk):
    relacion = get_object_or_404(RelacionesJerarquicas, pk=pk)

    if request.method == 'POST':
        form = RelacionJerarquicaForm(request.POST, instance=relacion)
        if form.is_valid():
            form.save()
            return redirect('listar_relaciones_jerarquicas')
    else:
        form = RelacionJerarquicaForm(instance=relacion)

    return render(request, 'relacion_jerarquica/editar_relacion_jerarquica.html', {'form': form})


# region cargos
# crear_cargo
def crear_cargo(request):
    if request.method == 'POST':
        form = CargoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_cargos')
    else:
        form = CargoForm()
    return render(request, 'cargo/crear_cargo.html', {'form': form})

# listar_cargos
def listar_cargos(request):
    cargos = Cargo.objects.all()
    return render(request, 'cargo/listar_cargos.html', {'cargos': cargos})

# actualizar_cargo
def actualizar_cargo(request, cargo_id):
    cargo = get_object_or_404(Cargo, id=cargo_id)
    if request.method == 'POST':
        form = CargoForm(request.POST, instance=cargo)
        if form.is_valid():
            form.save()
            return redirect('listar_cargos')
    else:
        form = CargoForm(instance=cargo)
    return render(request, 'cargo/actualizar_cargo.html', {'form': form})

# eliminar_cargo
def eliminar_cargo(request, cargo_id):
    cargo = get_object_or_404(Cargo, id=cargo_id)
    cargo.delete()
    return redirect('listar_cargos')
