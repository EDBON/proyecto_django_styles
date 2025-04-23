"""
URL configuration for clinic_master project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from clinic_master_app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

urlpatterns = [
    # region lagin
    path("", views.login_view, name="login"),
    
    path('mis_citas/', views.filtrar_mis_citas, name='filtrar_mis_citas'),
    
    path('activar_cita/<int:cita_id>/', views.activar_cita, name='activar_cita'),
    path('citas-inactivas/', views.seleccionar_cita, name='seleccionar_cita'),
    # region listar_citas_activas
    path('citas-activas/', views.listar_citas_activas, name='listar_citas_activas'),
    
    # region usuario
    path('crear_usuario/', views.crear_usuario, name='crear_usuario'),
    path('listar_usuarios/', views.listar_usuarios, name='listar_usuarios'),
    path('actualizar_usuario/<int:usuario_id>/', views.actualizar_usuario, name='actualizar_usuario'),
    path('eliminar_usuario/<int:usuario_id>/', views.eliminar_usuario, name='eliminar_usuario'),
    
    
    

    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
    
    # home
    path("home/", views.home, name="home"),
    path("medico/", views.medico, name="medico"),
    path("auxiliar/", views.auxiliar, name="auxiliar"),
    path("persona/", views.persona, name="persona"),
    
    # region Rutas para Eps
    path('crear_eps/', views.crear_eps, name='crear_eps'),
    path('listar_eps/', views.listar_eps, name='listar_eps'),
    path('actualizar_eps/<int:eps_id>/', views.actualizar_eps, name='actualizar_eps'),
    path('eliminar_eps/<int:eps_id>/', views.eliminar_eps, name='eliminar_eps'),

    # region Rutas para Persona
    path('crear_persona/', views.crear_persona, name='crear_persona'),
    path('listar_personas/', views.listar_personas, name='listar_personas'),
    path('actualizar_persona/<int:persona_id>/', views.actualizar_persona, name='actualizar_persona'),
    path('desactivar_persona/<int:persona_id>/', views.desactivar_persona, name='desactivar_persona'),
    path('personas/inactivas/', views.listar_personas_inactivas, name='listar_personas_inactivas'),
    path('reactivar_persona/<int:id>/', views.reactivar_persona, name='reactivar_persona'),

    # region Rutas para Contrato
    path('crear_contrato/', views.crear_contrato, name='crear_contrato'),
    path('listar_contrato/', views.listar_contratos, name='listar_contratos'),
    path('actualizar_contrato/<int:contrato_id>/', views.actualizar_contrato, name='actualizar_contrato'),
    path('eliminar_contrato/<int:contrato_id>/', views.eliminar_contrato, name='eliminar_contrato'),

    # region Rutas para Formacion
    path('crear_formacion/', views.crear_formacion, name='crear_formacion'),
    path('listar_formacion/', views.listar_formaciones, name='listar_formaciones'),
    path('actualizar_formacion/<int:formacion_id>/', views.actualizar_formacion, name='actualizar_formacion'),
    path('eliminar_formacion/<int:formacion_id>/', views.eliminar_formacion, name='eliminar_formacion'),

    # region Rutas para Empleado
    path('crear_empleado/', views.crear_empleado, name='crear_empleado'),
    path('listar_empleado/', views.listar_empleados, name='listar_empleados'),
    path('actualizar_empleado/<int:empleado_id>/', views.actualizar_empleado, name='actualizar_empleado'),
    path('eliminar_empleado/<int:empleado_id>/', views.eliminar_empleado, name='eliminar_empleado'),

    # region Rutas para Cita
    path('crear_cita/', views.crear_cita, name='crear_cita'),
    path('listar_citas/', views.listar_citas, name='listar_citas'),
    path('actualizar_cita/<int:cita_id>/', views.actualizar_cita, name='actualizar_cita'),
    path('eliminar_cita/<int:cita_id>/', views.eliminar_cita, name='eliminar_cita'),

    # region Rutas para Procedimiento
    path('crear_procedimiento/', views.crear_procedimiento, name='crear_procedimiento'),
    path('listar_procedimiento/', views.listar_procedimiento, name='listar_procedimiento'),
    path('actualizar_procedimiento/<int:procedimiento_id>/', views.actualizar_procedimiento, name='actualizar_procedimiento'),
    path('eliminar_procedimiento/<int:procedimiento_id>/', views.eliminar_procedimiento, name='eliminar_procedimiento'),

    #region  Rutas para Sala
    path('crear_sala/', views.crear_sala, name='crear_sala'),
    path('listar_sala/', views.listar_salas, name='listar_salas'),
    path('actualizar_sala/<int:sala_id>/', views.actualizar_sala, name='actualizar_sala'),
    path('eliminar_sala/<int:sala_id>/', views.eliminar_sala, name='eliminar_sala'),

    # region Rutas para Diagnostico
    path('crear_diagnostico/<int:consulta_id>/', views.crear_diagnostico, name='crear_diagnostico'),
    path('listar_diagnosticos/', views.listar_diagnosticos, name='listar_diagnosticos'),
    path('actualizar_diagnostico/<int:diagnostico_id>/', views.actualizar_diagnostico, name='actualizar_diagnostico'),
    path('eliminar_diagnostico/<int:diagnostico_id>/', views.eliminar_diagnostico, name='eliminar_diagnostico'),

    # region Rutas para Anamnesis
    path('crear_anamnesis/', views.crear_anamnesis, name='crear_anamnesis'),
    path('listar_anamnesis/', views.listar_anamnesis, name='listar_anamnesis'),
    path('actualizar_anamnesis/<int:anamnesis_id>/', views.actualizar_anamnesis, name='actualizar_anamnesis'),
    path('eliminar_anamnesis/<int:anamnesis_id>/', views.eliminar_anamnesis, name='eliminar_anamnesis'),

    # region Rutas para ExploracionFisica
    path('crear_exploracion_fisica/', views.crear_exploracion_fisica, name='crear_exploracion_fisica'),
    path('listar_exploracion_fisica/', views.listar_exploraciones_fisica, name='listar_exploracion_fisica'),
    path('actualizar_exploracion_fisica/<int:exploracion_fisica_id>/', views.actualizar_exploracion_fisica, name='actualizar_exploracion_fisica'),
    path('eliminar_exploracion_fisica/<int:exploracion_fisica_id>/', views.eliminar_exploracion_fisica, name='eliminar_exploracion_fisica'),

    # region Rutas para Consulta
    path('consulta/crear/<int:cita_id>/', views.crear_consulta, name='crear_consulta'),
    path('listar_consulta/', views.listar_consultas, name='listar_consultas'),
    path('actualizar_consulta/<int:consulta_id>/', views.actualizar_consulta, name='actualizar_consulta'),
    path('eliminar_consulta/<int:consulta_id>/', views.eliminar_consulta, name='eliminar_consulta'),

    # region Rutas para Medicamento
    path('crear_medicamento/', views.crear_medicamento, name='crear_medicamento'),
    path('listar_medicamento/', views.listar_medicamento, name='listar_medicamento'),
    path('actualizar_medicamento/<int:medicamento_id>/', views.actualizar_medicamento, name='actualizar_medicamento'),
    path('eliminar_medicamento/<int:medicamento_id>/', views.eliminar_medicamento, name='eliminar_medicamento'),

    # region Rutas para Formula
    path('crear_formula/', views.crear_formula, name='crear_formula'),
    path('listar_formula/', views.listar_formula, name='listar_formula'),
    path('actualizar_formula/<int:formula_id>/', views.actualizar_formula, name='actualizar_formula'),
    path('eliminar_formula/<int:formula_id>/', views.eliminar_formula, name='eliminar_formula'),

    # region Rutas para HistoriaClinica
    path('historia_clinica/<int:persona_id>/', views.ver_historia_clinica, name='ver_historia_clinica'),path('historia_clinica/<int:persona_id>/', views.ver_historia_clinica, name='ver_historia_clinica'),
    path('crear_historia_clinica/', views.crear_historia_clinica, name='crear_historia_clinica'),
    path('listar_historia_clinica/', views.listar_historias_clinicas, name='listar_historia_clinica'),
    path('actualizar_historia_clinica/<int:historia_clinica_id>/', views.actualizar_historia_clinica, name='actualizar_historia_clinica'),
    path('eliminar_historia_clinica/<int:historia_clinica_id>/', views.eliminar_historia_clinica, name='eliminar_historia_clinica'),
    path('consulta/<int:consulta_id>/', views.detalle_consulta, name='detalle_consulta'),
    # region api_empleados por especialidad
    path('ajax/medico-por-cita/', views.obtener_medico_por_cita, name='obtener_medico_por_cita'),
    path('api/empleados/', views.empleados_por_especialidad, name='api_empleados_por_especialidad'),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
