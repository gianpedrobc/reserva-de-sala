from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.db.models import Q
from datetime import time


class Espaco(models.Model):
    """Modelo para representar salas e laboratórios disponíveis para reserva."""
    
    class TipoEspaco(models.TextChoices):
        SALA = 'sala', 'Sala'
        LABORATORIO = 'lab', 'Laboratório'
    
    nome = models.CharField(max_length=100, unique=True)
    tipo = models.CharField(max_length=10, choices=TipoEspaco.choices)
    capacidade = models.PositiveIntegerField()
    possui_computadores = models.BooleanField(default=False)
    descricao = models.TextField(blank=True, null=True, default="Sem descrição")
    
    class Meta:
        ordering = ['nome']
        indexes = [
            models.Index(fields=['tipo']),
            models.Index(fields=['capacidade']),
        ]
    
    def __str__(self):
        return f"{self.nome} ({self.get_tipo_display()})"


class Reserva(models.Model):
    """Modelo para representar reservas de espaços com validação de conflitos."""
    
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservas')
    espaco = models.ForeignKey(Espaco, on_delete=models.CASCADE, related_name='reservas')
    data = models.DateField()
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()
    descricao = models.CharField(max_length=255, blank=True)
    
    class Meta:
        ordering = ['-data', 'hora_inicio']
        indexes = [
            models.Index(fields=['data']),
            models.Index(fields=['espaco']),
            models.Index(fields=['usuario']),
        ]
    
    def __str__(self):
        return f"{self.espaco} - {self.data} ({self.hora_inicio} a {self.hora_fim})"
    
    def clean(self):
        """
        Validação de regras de negócio:
        1. Hora inicio < Hora fim
        2. Data não pode ser no passado
        3. Não pode haver sobreposição de horários para o mesmo espaço na mesma data
        """
        
        # Validar: hora_inicio < hora_fim
        if self.hora_inicio >= self.hora_fim:
            raise ValidationError("A hora de início deve ser anterior à hora de término.")
        
        # Validar: data não pode ser no passado
        if self.data < timezone.now().date():
            raise ValidationError("Não é possível agendar reservas para datas que já passaram.")
        
        # Validar: sem sobreposição de horários
        # Lógica: A nova reserva NÃO pode estar sobreposta a nenhuma reserva existente
        # Sobrepõe-se quando: (nova_inicio < existente_fim) AND (nova_fim > existente_inicio)
        conflito = Reserva.objects.filter(
            espaco=self.espaco,
            data=self.data
        ).filter(
            Q(hora_inicio__lt=self.hora_fim) & Q(hora_fim__gt=self.hora_inicio)
        )
        
        # Se for um update, excluir o próprio registro da verificação
        if self.pk:
            conflito = conflito.exclude(pk=self.pk)
        
        if conflito.exists():
            raise ValidationError(
                f"Este espaço já está reservado para o horário selecionado "
                f"({conflito.first().hora_inicio} a {conflito.first().hora_fim}). "
                f"Por favor, escolha outro horário."
            )
    
    def save(self, *args, **kwargs):
        """Chamar clean() antes de salvar."""
        self.full_clean()
        super().save(*args, **kwargs)
