"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path
from reservas import views

urlpatterns = [
    path('', views.lista_salas, name='lista_salas'),
    path('admin/', admin.site.urls),
]
