@echo off
REM Script para iniciar o servidor Django - Windows

echo.
echo =======================================================
echo Sistema de Reserva de Salas e Laboratorios
echo =======================================================
echo.

REM Mostrar IP da máquina
echo Seu IP na rede:
ipconfig | findstr /i "IPv4"

echo.

REM Ativar ambiente virtual
call .\venv\Scripts\Activate.bat

REM Iniciar servidor acessível na rede
echo Iniciando servidor...
python manage.py runserver 0.0.0.0:8000

pause
