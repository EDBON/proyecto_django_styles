from django import forms
from .models import *
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm,UserCreationForm
from django_select2.forms import Select2MultipleWidget
from django.contrib.auth import authenticate
from django_select2.forms import ModelSelect2Widget

CARGOS = [
    ("medico_general", "Médico General"),
    ("medico_especialista", "Médico Especialista"),
    ("enfermero_jefe", "Enfermero(a) Jefe"),
    ("auxiliar_enfermeria", "Auxiliar de Enfermería"),
    ("terapista", "Terapista (Físico, Ocupacional, Respiratorio, etc.)"),
    ("bacteriologo", "Bacteriólogo(a)"),
    ("director_medico", "Gerente o Director Médico"),
    ("coordinador_salud", "Coordinador de Servicios de Salud"),
    ("recepcionista", "Recepcionista / Auxiliar Administrativo"),
    ("facturador", "Facturador o Auxiliar de Cuentas Médicas"),
    ("trabajador_social", "Trabajador Social"),
    ("regente_farmacia", "Regente de Farmacia"),
    ("tecnico_radiologia", "Técnico en Radiología"),
    ("aseo_mantenimiento", "Personal de Aseo y Mantenimiento"),
]

# region login form
class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Usuario", max_length=100)
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)

# region  usuario form
class UsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ["persona","username", "puesto_empresa", "password1", "password2"]
        widgets = {
            'persona': forms.Select(attrs={'class': 'select2 form-select'}),
        }

class UsuarioUpdateForm(UserChangeForm):
    password = None  # Oculta el campo de contraseña

    class Meta:
        model = Usuario
        fields = ['persona', 'username', 'puesto_empresa']



# region eps form
class EpsForm(forms.ModelForm):
    class Meta:
        model = Eps
        fields = '__all__'
        
# region persona form
class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'
        widgets = {
            'fecha_nac': forms.DateInput(format='%Y-%m-%d', attrs={'class': 'flatpickr'}),
            
        }

# region contrato form
class ContratoForm(forms.ModelForm):
    class Meta:
        model = Contrato
        fields = '__all__'


# region formacion form
class FormacionForm(forms.ModelForm):
    class Meta:
        model = Formacion
        fields = '__all__'
        widgets = { 
            
            'fecha_inicio': forms.DateInput(
                format='%Y-%m-%d',
                attrs={'class': 'flatpickr'}
            ),
            'fecha_fin': forms.DateInput(
                format='%Y-%m-%d',
                attrs={'class': 'flatpickr'}
            ),
            
        }


# region empleado form
class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'
        widgets = {
            'area_trabajo': forms.Select(attrs={'class': 'select2 form-select'}),
            'especialidades': forms.Select(attrs={'class': 'select2 form-select'}),
            'id_persona': forms.Select(attrs={'class': 'select2 form-select'}),
        }

# region documento_empleado form
class DocumentoEmpleadoForm(forms.ModelForm):
    class Meta:
        model = DocumentosEmpleado
        fields = '__all__'
        widgets = {
            'empleado': forms.Select(attrs={'class': 'select2 form-select'}),
            'fecha': forms.DateInput(attrs={'class': 'flatpickr'}),
        }
# region historial_movimiento form
class HistorialMovimientoForm(forms.ModelForm):
    class Meta:
        model = HistorialMovimientos
        fields = '__all__'
        widgets = {
            'empleado': forms.Select(attrs={'class': 'select2 form-select'}),
            'fecha_movimiento': forms.DateInput(attrs={'class': 'flatpickr'}),
        }

# region relacion_jerarquica form
class RelacionJerarquicaForm(forms.ModelForm):
    class Meta:
        model = RelacionesJerarquicas
        fields = '__all__'
        widgets = {
            'supervisor': forms.Select(attrs={'class': 'select2 form-select'}),
            'subordinado': forms.Select(attrs={'class': 'select2 form-select'}),
        }
# region cargo form
class CargoForm(forms.ModelForm):
    class Meta:
        model = Cargo
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
