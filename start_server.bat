@echo off
REM Script para iniciar o servidor Django - Windows

echo.
echo =======================================================
echo Sistema de Reserva de Salas e Laboratorios
echo =======================================================
echo.

REM Ativar ambiente virtual
call .\venv\Scripts\Activate.ps1

REM Iniciar servidor
echo Iniciando servidor...
python manage.py runserver

pause
