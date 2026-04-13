"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path
from reservas import views

urlpatterns = [
    # Salas
    path('', views.lista_salas, name='lista_salas'),
    path('disponibilidade/', views.disponibilidade, name='disponibilidade'),
    
    # Reservas
    path('reserva/criar/', views.criar_reserva, name='criar_reserva'),
    path('reserva/<int:pk>/', views.detalhar_reserva, name='detalhar_reserva'),
    path('reserva/<int:pk>/editar/', views.editar_reserva, name='editar_reserva'),
    path('reserva/<int:pk>/cancelar/', views.cancelar_reserva, name='cancelar_reserva'),
    path('minhas-reservas/', views.minhas_reservas, name='minhas_reservas'),
    
    # Autenticação
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registrar/', views.registrar, name='registrar'),
    
    # Admin
    path('admin/', admin.site.urls),
]
