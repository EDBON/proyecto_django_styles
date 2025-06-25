from django import forms
from .models import *
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm,UserCreationForm
from django_select2.forms import Select2MultipleWidget
from django.contrib.auth import authenticate
from django_select2.forms import ModelSelect2Widget


# region Login Form
class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Usuario", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={'class': 'form-control'}))

# region Usuario Form
class UsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ["persona", "username", "puesto_empresa", "password1", "password2"]
        widgets = {
            'persona': forms.Select(attrs={'class': 'select2 form-select'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'puesto_empresa': forms.Select(attrs={'class': 'form-select'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

class UsuarioUpdateForm(UserChangeForm):
    password = None  # Oculta el campo de contraseña

    class Meta:
        model = Usuario
        fields = ['persona', 'username', 'puesto_empresa']
        widgets = {
            'persona': forms.Select(attrs={'class': 'select2 form-select'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'puesto_empresa': forms.Select(attrs={'class': 'form-select'}),
        }

# region EPS Form
class EpsForm(forms.ModelForm):
    class Meta:
        model = Eps
        fields = '__all__'
        widgets = {
            'nombre_eps': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion_eps': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono_eps': forms.TextInput(attrs={'class': 'form-control'}),
            'email_eps': forms.EmailInput(attrs={'class': 'form-control'}),
        }

# region Persona Form
class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'
        widgets = {
            'tipo_doc': forms.Select(attrs={'class': 'form-select'}),
            'num_doc': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_nac': forms.DateInput(format='%Y-%m-%d', attrs={'class': 'flatpickr form-control'}),
            'genero': forms.Select(attrs={'class': 'form-select'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'eps': forms.Select(attrs={'class': 'select2 form-select'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

# region Contrato Form
class ContratoForm(forms.ModelForm):
    class Meta:
        model = Contrato
        fields = '__all__'
        widgets = {
            'id_empleado': forms.Select(attrs={'class': 'select2 form-select'}),
            'salario': forms.NumberInput(attrs={'class': 'form-control'}),
            'tipo_contrato': forms.Select(attrs={'class': 'form-select'}),
            'fecha_inicio': forms.DateInput(format='%Y-%m-%d', attrs={'class': 'flatpickr form-control'}),
            'fecha_fin': forms.DateInput(format='%Y-%m-%d', attrs={'class': 'flatpickr form-control'}),
            'documento_contrato': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

# region Formacion Form
class FormacionForm(forms.ModelForm):
    class Meta:
        model = Formacion
        exclude = ['id_empleado']  # Ocultamos este campo porque lo asignamos desde la vista
        widgets = {
            'tipo_formacion': forms.TextInput(attrs={'class': 'form-control'}),
            'intitucion': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_inicio': forms.DateInput(
                format='%Y-%m-%d',
                attrs={'class': 'flatpickr form-control', 'type': 'date'}
            ),
            'fecha_fin': forms.DateInput(
                format='%Y-%m-%d',
                attrs={'class': 'flatpickr form-control', 'type': 'date'}
            ),
            'titulo_obtenido': forms.TextInput(attrs={'class': 'form-control'}),
        }

# region Empleado Form
class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'
        widgets = {
            'id_persona': forms.Select(attrs={'class': 'select2 form-select'}),
            'area_trabajo': forms.Select(attrs={'class': 'form-select'}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
            'puesto_empresa': forms.Select(attrs={'class': 'form-select'}),
            'especialidades': forms.Select(attrs={'class': 'form-select'}),
        }

# region DocumentosEmpleado Form
class DocumentoEmpleadoForm(forms.ModelForm):
    class Meta:
        model = DocumentosEmpleado
        exclude = ['id_empleado','subido_por']  # Se asigna desde la vista
        widgets = {
            'tipo_documento': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_documento': forms.TextInput(attrs={'class': 'form-control'}),
            'archivo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
        

# region HistorialMovimiento Form
class HistorialMovimientoForm(forms.ModelForm):
    class Meta:
        model = HistorialMovimientos
        fields = '__all__'
        widgets = {
            'empleado': forms.Select(attrs={'class': 'select2 form-select'}),
            'area_anterior': forms.TextInput(attrs={'class': 'form-control'}),
            'estado_anterior': forms.TextInput(attrs={'class': 'form-control'}),
            'area_nueva': forms.TextInput(attrs={'class': 'form-control'}),
            'estado_nuevo': forms.TextInput(attrs={'class': 'form-control'}),
            'motivo': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'fecha_movimiento': forms.DateInput(format='%Y-%m-%d', attrs={'class': 'flatpickr form-control'}),
            'registrado_por': forms.Select(attrs={'class': 'select2 form-select'}),
        }

# region RelacionesJerarquicas Form
class RelacionJerarquicaForm(forms.ModelForm):
    class Meta:
        model = RelacionesJerarquicas
        fields = '__all__'
        widgets = {
            'jefe': forms.Select(attrs={'class': 'select2 form-select'}),
            'subordinado': forms.Select(attrs={'class': 'select2 form-select'}),
            'fecha_inicio': forms.DateInput(format='%Y-%m-%d', attrs={'class': 'flatpickr form-control'}),
            'fecha_fin': forms.DateInput(format='%Y-%m-%d', attrs={'class': 'flatpickr form-control'}),
        }

# region Cargo Form
class CargoForm(forms.ModelForm):
    class Meta:
        model = Cargo
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'nivel_minimo': forms.Select(attrs={'class': 'form-select'}),
        }
