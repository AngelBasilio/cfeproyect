from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pensiones/', views.pensiones, name='pensiones'),
    path('pensiones/editar/<int:pk>/', views.editar_pensionado, name='editar_pensionado'),
    path('pensiones/eliminar/<int:pk>/', views.eliminar_pensionado, name='eliminar_pensionado'),
    path('trabajadores/', views.trabajadores, name='trabajadores'),
    path('trabajadores/editar/<int:pk>/', views.editar_trabajador, name='editar_trabajador'),
    path('trabajadores/eliminar/<int:pk>/', views.eliminar_trabajador, name='eliminar_trabajador'),
]
