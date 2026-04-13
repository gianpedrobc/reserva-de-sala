from django.shortcuts import render
from .models import Espaco

def lista_salas(request):
    """Busca todas as salas/labs cadastradas e exibe no template."""
    espacos = Espaco.objects.all()
    return render(request, 'salas/Listagem.html', {'salas': espacos})