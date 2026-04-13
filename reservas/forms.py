from django import forms
from .models import Reserva
from datetime import date


class ReservaForm(forms.ModelForm):
    """Formulário para criar/editar reservas com validações."""
    
    class Meta:
        model = Reserva
        fields = ['espaco', 'data', 'hora_inicio', 'hora_fim', 'descricao']
        widgets = {
            'espaco': forms.Select(attrs={'class': 'form-control'}),
            'data': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'min': date.today().isoformat()
            }),
            'hora_inicio': forms.TimeInput(attrs={
                'class': 'form-control',
                'type': 'time'
            }),
            'hora_fim': forms.TimeInput(attrs={
                'class': 'form-control',
                'type': 'time'
            }),
            'descricao': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Motivo da reserva (opcional)'
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['espaco'].queryset = self.fields['espaco'].queryset.order_by('nome')
