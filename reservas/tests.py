from django.test import TestCase
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from datetime import date, time, timedelta
from .models import Espaco, Reserva


class ReservaConflitosTestCase(TestCase):
    """Testes para validação de conflitos de horário."""
    
    def setUp(self):
        """Configurar dados para os testes."""
        self.usuario = User.objects.create_user(
            username='teste',
            password='12345'
        )
        self.espaco = Espaco.objects.create(
            nome='Laboratório de Informática',
            tipo='lab',
            capacidade=30,
            possui_computadores=True
        )
        self.data_teste = date.today() + timedelta(days=1)
    
    def test_reserva_sobreposta_deve_lancar_erro(self):
        """Testa se tentativa de sobrepor reservas lança ValidationError."""
        
        # Criar primeira reserva
        reserva1 = Reserva(
            usuario=self.usuario,
            espaco=self.espaco,
            data=self.data_teste,
            hora_inicio=time(10, 0),
            hora_fim=time(11, 0)
        )
        reserva1.save()
        
        # Tentar criar reserva sobreposta (10:30 - 11:30)
        reserva2 = Reserva(
            usuario=self.usuario,
            espaco=self.espaco,
            data=self.data_teste,
            hora_inicio=time(10, 30),
            hora_fim=time(11, 30)
        )
        
        # Deve lançar ValidationError
        with self.assertRaises(ValidationError):
            reserva2.save()
    
    def test_reserva_adjacente_deve_ser_permitida(self):
        """Testa se reservas em horários adjacentes são permitidas."""
        
        # Criar primeira reserva
        reserva1 = Reserva(
            usuario=self.usuario,
            espaco=self.espaco,
            data=self.data_teste,
            hora_inicio=time(10, 0),
            hora_fim=time(11, 0)
        )
        reserva1.save()
        
        # Criar segunda reserva iniciando quando a primeira termina
        reserva2 = Reserva(
            usuario=self.usuario,
            espaco=self.espaco,
            data=self.data_teste,
            hora_inicio=time(11, 0),
            hora_fim=time(12, 0)
        )
        
        # Não deve lançar erro
        reserva2.save()
        self.assertEqual(Reserva.objects.count(), 2)
    
    def test_data_no_passado_deve_lancar_erro(self):
        """Testa se agendamento em data passada lança erro."""
        
        reserva = Reserva(
            usuario=self.usuario,
            espaco=self.espaco,
            data=date.today() - timedelta(days=1),
            hora_inicio=time(10, 0),
            hora_fim=time(11, 0)
        )
        
        with self.assertRaises(ValidationError):
            reserva.save()
