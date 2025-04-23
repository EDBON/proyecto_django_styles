from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
import os
import ast

TIPO_DOC = [
    ('CC', 'Cédula de Ciudadanía'),
    ('TI', 'Tarjeta de Identidad'),
    ('CE', 'Cédula de Extranjería'),
]

MEDICAMENTOS = [
    ('ninguno', 'Ninguno'),
    ('acetaminofen', 'Acetaminofén'),
    ('ibuprofeno', 'Ibuprofeno'),
    ('amoxicilina', 'Amoxicilina'),
    ('loratadina', 'Loratadina'),
    ('omeprazol', 'Omeprazol'),
    ('salbutamol', 'Salbutamol'),
    ('metformina', 'Metformina'),
    ('losartán', 'Losartán'),
    ('enalapril', 'Enalapril'),
]


GENERO = [
    ('M', 'Masculino'),
    ('F', 'Femenino'),
]

NIVELES_IPS = [
    (1, "Nivel 1 - Básico"),
    (2, "Nivel 2 - Intermedio"),
    (3, "Nivel 3 - Avanzado"),
]
# region list especialidades

ESPECIALIDADES = [
    ('Ninguno', 'ninguno'),
    ('Medicina General', 'Atención médica básica'),
    ('Cardiología', 'Enfermedades del corazón'),
    ('Neumología', 'Enfermedades respiratorias'),
    ('Gastroenterología', 'Trastornos digestivos'),
    ('Dermatología', 'Enfermedades de la piel'),
    ('Pediatría', 'Atención a niños y adolescentes'),
    ('Obstetricia y Ginecología', 'Salud femenina y embarazo'),
    ('Neurología', 'Enfermedades del sistema nervioso'),
    ('Oncología', 'Tratamiento del cáncer'),
    ('Psiquiatría', 'Trastornos mentales y emocionales'),
    ('Cirugía General', 'Intervenciones quirúrgicas comunes'),
    ('Ortopedia', 'Trastornos del sistema musculoesquelético'),
    ('Oftalmología', 'Enfermedades de los ojos'),
    ('Radiología', 'Diagnóstico por imágenes'),
    ('Anestesiología', 'Anestesia en procedimientos quirúrgicos'),
]
# region list puestos

PUESTOS = [
    ("Puesto clínico", "Médico general"),
    ("Puesto clínico", "Enfermero(a)"),
    ("Puesto clínico", "Auxiliar de enfermería"),
    ("Puesto clínico", "Especialistas médicos"),
    ("Puesto administrativo", "Gerente médico"),
    ("Puesto administrativo", "Gerente administrativo"),
    ("Puesto administrativo", "Recepcionista"),
    ("Puesto administrativo", "Contador(a)"),
    ("Otros puestos", "Técnico en sistemas"),
    ("it", "IT")
]
# region list_puestos de area de trabajo


PUESTOS_AREA_TRABAJO = [
    ("Médico general", "Consultorio médico"),
    ("Enfermero(a)", "Área de atención a pacientes"),
    ("Auxiliar de enfermería", "Área de atención a pacientes"),
    ("Especialistas médicos", "Consultorio especializado"),
    ("Gerente médico", "Oficina administrativa médica"),
    ("Gerente administrativo", "Oficina administrativa"),
    ("Recepcionista", "Recepción y gestión de citas"),
    ("Contador(a)", "Departamento de contabilidad y finanzas"),
    ("Técnico en sistemas", "Departamento de tecnología y soporte")
]
# region list_puestos_contrato
PUESTOS_CONTRATO = [
    ("Médico general", "Contrato a término indefinido"),
    ("Enfermero(a)", "Contrato a término indefinido"),
    ("Auxiliar de enfermería", "Contrato a término fijo"),
    ("Especialistas médicos", "Contrato por prestación de servicios"),
    ("Gerente médico", "Contrato a término indefinido"),
    ("Gerente administrativo", "Contrato a término indefinido"),
    ("Recepcionista", "Contrato a término fijo"),
    ("Contador(a)", "Contrato a término indefinido"),
    ("Técnico en sistemas", "Contrato por prestación de servicios")
]


def user_directory_path(instance, filename):
    return f"persona/img/{instance.id}_{filename}"
def user_directory_path_1(instance, filename):
    return f"persona/file/{instance.id}_{filename}"



#region EPS    
class Eps(models.Model):
    nombre_eps  = models.CharField(max_length=100)
    direccion_eps = models.CharField(max_length=100)
    telefono_eps = models.CharField(max_length=15)
    email_eps = models.EmailField(max_length=100)
    
    def __str__(self):
        return self.nombre_eps
    
#region Cargo
class Cargo(models.Model):
    nombre = models.CharField(max_length=100)
    nivel_minimo = models.IntegerField(choices=NIVELES_IPS, default=1)
    
    def __str__(self):
        return self.nombre

#region Persona
class Persona(models.Model):
    tipo_doc = models.CharField(max_length=10, choices=TIPO_DOC)
    num_doc = models.CharField(max_length=10, unique=True, null=False)
    def clean(self):
        # Asegura que el valor de num_doc solo contenga dígitos
        if self.num_doc and not self.num_doc.isdigit():
            raise ValidationError('El número de documento solo puede contener dígitos numericos.')
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nac = models.DateField()
    genero = models.CharField(max_length=50, choices=GENERO)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()
    eps = models.ForeignKey(Eps, on_delete=models.CASCADE, null=True)
    is_active = models.BooleanField(default=True)
    imagen = models.ImageField(upload_to=user_directory_path, blank=True, null=True, verbose_name='imagen')
    def __str__(self):
        return f'{self.num_doc} - {self.nombre}'
    
    

#region Empleado
class Empleado(models.Model):
    id_persona = models.ForeignKey(Persona, on_delete=models.CASCADE, null=True)
    area_trabajo = models.CharField(max_length=100, choices=PUESTOS_AREA_TRABAJO)
    estado = models.CharField(max_length=20,
        choices=[
            ('Activo', 'Activo'),
            ('Inactivo', 'Inactivo'),
            ('Suspendido', 'Suspendido')],default='Activo')
    puesto_empresa = models.CharField(max_length=100, choices=PUESTOS)
    especialidades = models.CharField(max_length=100 , choices=ESPECIALIDADES, null=True) 
    
    def __str__(self):
        return f'{self.id_persona}'
    
    
#region Usuario

class Usuario(AbstractUser):
    persona = models.OneToOneField('Persona', on_delete=models.SET_NULL, null=True, blank=True)  # <- esta línea nueva

    puesto_empresa = models.CharField(
        max_length=50,
        choices=[
            ("it", "IT"),
            ("medico", "Médico"),
            ("admin", "Administrador"),
            ("persona", "persona"),
            ("auxiliar", "Auxiliar"),
        ],
        default="it"
    )

    def __str__(self):
        return self.username
    
#region Formacion
class Formacion(models.Model):
    tipo_formacion = models.CharField(max_length=100)
    intitucion = models.CharField(max_length=100)
    fecha_inicio = models.DateField(max_length=100)
    fecha_fin = models.DateField(max_length=100)
    titulo_obtenido = models.CharField(max_length=100)
    id_empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, null=True)
    
    
#region Contrato
class Contrato(models.Model):
    id_empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE,null=True)
    salario = models.DecimalField(max_digits=10, decimal_places=2)  # Mejor usar DecimalField para valores monetarios
    tipo_contrato = models.CharField(max_length=100, choices=PUESTOS_CONTRATO)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_fin = models.DateField(blank=True, null=True)
    documento_contrato = models.FileField(upload_to=user_directory_path_1, blank=True, null=True, verbose_name='Contrato')
    @property
    def archivo_nombre(self):
        return os.path.basename(self.documento_contrato.name).replace("None_", "")
    
    




#region Procedimiento
class Procedimiento(models.Model):
    nombre_procedimiento = models.CharField(max_length=50)
    descripcion_procedimiento = models.TextField()
    duracion_estimada = models.CharField(max_length=40)
    
    
#region Sala
class Sala(models.Model):
    nombre_sala = models.CharField(max_length=50)
    ubicacion_sala = models.CharField(max_length=100)
    capacidad_sala = models.CharField(max_length=100)
    disponibilidad_inicio = models.TimeField(null=True, blank=True)
    disponibilidad_fin = models.TimeField(null=True, blank=True)
    
    def __str__(self):
        return f'Sala{self.ubicacion_sala}'


#region Cita
class Cita(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, null=True,blank=True)
    sala= models.ForeignKey(Sala,on_delete=models.CASCADE,null=True,blank=True )
    hora = models.TimeField()
    fecha = models.DateField()
    tipo = models.CharField(max_length=100, choices=ESPECIALIDADES) 
    is_active = models.BooleanField(default=True)
    id_empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'Cita de {self.persona.nombre} el {self.fecha} a las {self.hora}'

#region Diagnostico     
class Diagnostico(models.Model):
    diagnostico_principal = models.TextField()
    pruebas_complementarias = models.TextField()
    interpretacion_examen = models.CharField(max_length=100)
    diagnostico_final = models.TextField()

#region Medicamento
class Medicamento(models.Model):
    nombre_medicamento = models.CharField(max_length=100)
    dosis = models.CharField(max_length=100)
    frecuencia = models.CharField(max_length=100)
    duracion_tratamiento = models.CharField(max_length=100)
    cantidad_total = models.CharField(max_length=100)
    indicaciones_especiales = models.TextField()    
    
    
#region  Anamnesis
class Anamnesis(models.Model):
    cirugias = models.TextField()
    hospitalizacion = models.TextField()
    alergias = models.TextField()
    enfermedad_familiar = models.TextField()
    trabajo = models.TextField()
    fuma = models.TextField()
    ejercicio = models.TextField()
    medicamentos = models.CharField(
        max_length=50,
        choices=MEDICAMENTOS,
        default='ninguno',
        null=True,
        blank=True
    )
    
#region Exploracion Fisica
class ExploracionFisica(models.Model):
    id_anamnesis = models.ForeignKey(Anamnesis, on_delete=models.CASCADE, null=True)
    frecuencia_cardiaca = models.PositiveIntegerField(null=True, blank=True)  
    temperatura = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)  
    presion_diastolica = models.PositiveIntegerField(null=True, blank=True)  
    saturacion_oxigeno = models.PositiveIntegerField(null=True, blank=True)  
    inspeccion_general = models.TextField(blank=True, null=True)
    cabeza_cuello = models.TextField(blank=True, null=True)
    torax_pulmones = models.TextField(blank=True, null=True)
    corazon = models.TextField(blank=True, null=True)
    abdomen = models.TextField(blank=True, null=True)
    extremidades = models.TextField(blank=True, null=True)
    sistema_nervioso = models.TextField(blank=True, null=True)


#region Consulta
class Consulta(models.Model):
    fecha = models.DateField()
    medico = models.ForeignKey(Empleado, on_delete=models.CASCADE, null=True)
    cita = models.ForeignKey(Cita, on_delete=models.CASCADE, null=True)
    id_anamnesis = models.ForeignKey(Anamnesis, on_delete=models.CASCADE, null=True)
    id_diagnostico = models.ForeignKey(Diagnostico, on_delete=models.CASCADE, null=True)
    
    
#region Formula
class Formula(models.Model):
    descripcion = models.TextField()
    id_diagnostico = models.ForeignKey(Diagnostico, on_delete=models.CASCADE, null=True)
    mid_nombre_medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE, null=True)
    fecha_expiracion  = models.DateField()
    recomendaciones_medicas = models.TextField()   


#region Historia Clinica
class Historia_clinica(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, null=True)
    consulta = models.ForeignKey(Consulta, on_delete=models.CASCADE, null=True)