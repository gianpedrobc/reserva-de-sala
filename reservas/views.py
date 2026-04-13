from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Q
from datetime import date, timedelta
from .models import Espaco, Reserva
from .forms import ReservaForm


# ===== LISTAGEM DE SALAS =====

def lista_salas(request):
    """Lista todas as salas/labs cadastradas com filtro opcional."""
    espacos = Espaco.objects.all()
    
    # Filtro por tipo
    tipo_filtro = request.GET.get('tipo', '')
    if tipo_filtro:
        espacos = espacos.filter(tipo=tipo_filtro)
    
    # Busca por nome
    busca = request.GET.get('q', '')
    if busca:
        espacos = espacos.filter(nome__icontains=busca)
    
    context = {
        'salas': espacos,
        'tipos': Espaco.TipoEspaco.choices,
        'tipo_filtro': tipo_filtro,
        'busca': busca,
    }
    return render(request, 'salas/Listagem.html', context)


# ===== RESERVAS =====

@login_required(login_url='login')
def criar_reserva(request):
    """Cria uma nova reserva."""
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)
            reserva.usuario = request.user
            try:
                reserva.save()
                messages.success(request, '✅ Reserva criada com sucesso!')
                return redirect('minhas_reservas')
            except Exception as e:
                messages.error(request, f'❌ Erro ao criar reserva: {str(e)}')
    else:
        form = ReservaForm()
    
    return render(request, 'reservas/criar.html', {'form': form})


@login_required(login_url='login')
def minhas_reservas(request):
    """Exibe as reservas do usuário logado."""
    reservas = request.user.reservas.all().order_by('-data')
    hoje = date.today()
    
    reservas_ativas = reservas.filter(data__gte=hoje)
    reservas_passadas = reservas.filter(data__lt=hoje)
    
    context = {
        'reservas_ativas': reservas_ativas,
        'reservas_passadas': reservas_passadas,
    }
    return render(request, 'reservas/minhas_reservas.html', context)


@login_required(login_url='login')
def detalhar_reserva(request, pk):
    """Exibe detalhes de uma reserva."""
    reserva = get_object_or_404(Reserva, pk=pk, usuario=request.user)
    return render(request, 'reservas/detalhe.html', {'reserva': reserva})


@login_required(login_url='login')
def editar_reserva(request, pk):
    """Edita uma reserva."""
    reserva = get_object_or_404(Reserva, pk=pk, usuario=request.user)
    
    # Não pode editar reservas passadas
    if reserva.data < date.today():
        messages.error(request, '❌ Não é possível editar reservas passadas!')
        return redirect('minhas_reservas')
    
    if request.method == 'POST':
        form = ReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, '✅ Reserva atualizada com sucesso!')
                return redirect('minhas_reservas')
            except Exception as e:
                messages.error(request, f'❌ Erro ao atualizar: {str(e)}')
    else:
        form = ReservaForm(instance=reserva)
    
    return render(request, 'reservas/editar.html', {'form': form, 'reserva': reserva})


@login_required(login_url='login')
def cancelar_reserva(request, pk):
    """Cancela uma reserva."""
    reserva = get_object_or_404(Reserva, pk=pk, usuario=request.user)
    
    # Não pode cancelar reservas passadas
    if reserva.data < date.today():
        messages.error(request, '❌ Não é possível cancelar reservas passadas!')
        return redirect('minhas_reservas')
    
    if request.method == 'POST':
        espaco = reserva.espaco.nome
        reserva.delete()
        messages.success(request, f'✅ Reserva de "{espaco}" cancelada!')
        return redirect('minhas_reservas')
    
    return render(request, 'reservas/confirmar_cancelamento.html', {'reserva': reserva})


# ===== DISPONIBILIDADE =====

def disponibilidade(request):
    """Exibe disponibilidade de salas por data."""
    data_filtro = request.GET.get('data', date.today().isoformat())
    
    try:
        data_filtro = date.fromisoformat(data_filtro)
    except:
        data_filtro = date.today()
    
    if data_filtro < date.today():
        data_filtro = date.today()
    
    espacos = Espaco.objects.all()
    
    # Para cada espaço, buscar reservas da data
    espacos_disponibilidade = []
    for espaco in espacos:
        reservas = Reserva.objects.filter(espaco=espaco, data=data_filtro).order_by('hora_inicio')
        espacos_disponibilidade.append({
            'espaco': espaco,
            'reservas': reservas,
            'disponivel': not reservas.exists()
        })
    
    context = {
        'data_filtro': data_filtro,
        'data_min': date.today().isoformat(),
        'espacos_disponibilidade': espacos_disponibilidade,
    }
    return render(request, 'reservas/disponibilidade.html', context)


# ===== AUTENTICAÇÃO =====

def login_view(request):
    """Login de usuário."""
    if request.user.is_authenticated:
        return redirect('lista_salas')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'✅ Bem-vindo, {user.username}!')
            return redirect('lista_salas')
        else:
            messages.error(request, '❌ Usuário ou senha inválidos!')
    
    return render(request, 'auth/login.html')


def logout_view(request):
    """Logout de usuário."""
    logout(request)
    messages.success(request, '✅ Deslogado com sucesso!')
    return redirect('login')


def registrar(request):
    """Registro de novo usuário."""
    if request.user.is_authenticated:
        return redirect('lista_salas')
    
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')
        password_confirm = request.POST.get('password_confirm', '')
        
        # Validações
        if not username or not email or not password:
            messages.error(request, '❌ Preencha todos os campos!')
        elif User.objects.filter(username=username).exists():
            messages.error(request, '❌ Este usuário já existe!')
        elif User.objects.filter(email=email).exists():
            messages.error(request, '❌ Este email já está cadastrado!')
        elif password != password_confirm:
            messages.error(request, '❌ As senhas não conferem!')
        elif len(password) < 6:
            messages.error(request, '❌ A senha deve ter pelo menos 6 caracteres!')
        elif len(username) < 3:
            messages.error(request, '❌ O usuário deve ter pelo menos 3 caracteres!')
        else:
            try:
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password
                )
                messages.success(request, '✅ Cadastro realizado com sucesso! Faça login agora.')
                return redirect('login')
            except Exception as e:
                messages.error(request, f'❌ Erro ao criar usuário: {str(e)}')
    
    return render(request, 'auth/registro.html')
