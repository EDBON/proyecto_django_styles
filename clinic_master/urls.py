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
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
