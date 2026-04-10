# 🚀 Sistema de Reserva de Salas e Laboratórios - Backend

## Status: ✅ Projeto Rodando

Backend Django completamente configurado e pronto para desenvolvimento.

---

## 📋 Checklist de Conclusão

- ✅ Ambiente Virtual (venv) criado
- ✅ Django instalado (requirements.txt gerado)
- ✅ Projeto `core` criado
- ✅ App `reservas` criada
- ✅ Models (Espaco e Reserva) implementados com validações
- ✅ Admin.py configurado com CRUDs
- ✅ Tests.py com 3 testes unitários (todos passando)
- ✅ Migrações criadas e aplicadas
- ✅ Banco de dados (SQLite) inicializado
- ✅ Superusuário criado

---

## 🔐 Credenciais Admin

**URL:** `http://localhost:8000/admin/`  
**Usuário:** `admin`  
**Senha:** `admin123`

---

## 🚀 Como Rodar o Servidor

### 1. Ativar o Ambiente Virtual

**Windows (PowerShell):**
```powershell
.\venv\Scripts\Activate.ps1
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

### 2. Iniciar o Servidor

```bash
python manage.py runserver
```

Acesse: `http://localhost:8000/`

---

## 📊 Estrutura do Projeto

```
reserva de sala/
├── venv/                     # Ambiente virtual
├── core/                     # Projeto Django
│   ├── settings.py          # Configurações
│   ├── urls.py              # Rotas principais
│   └── wsgi.py
├── reservas/                # App de reservas
│   ├── models.py            # Modelos (Espaco, Reserva)
│   ├── admin.py             # Painel administrativo
│   ├── tests.py             # Testes unitários
│   └── migrations/
├── manage.py
└── db.sqlite3               # Banco de dados
```

---

## 🧪 Testes

Executar todos os testes:
```bash
python manage.py test reservas
```

**Testes inclusos:**
- ✅ Detecção de reservas sobrepostas
- ✅ Permissão de horários adjacentes
- ✅ Validação de datas no passado

---

## 📦 Dependências Instaladas

```
Django 6.0.4
asgiref 3.11.1
sqlparse 0.5.5
tzdata 2026.1
```

---

## 📝 Modelo de Dados

### Espaco
- `nome` (CharField, único)
- `tipo` (TextChoices: Sala / Laboratório)
- `capacidade` (PositiveIntegerField)
- `possui_computadores` (BooleanField)

### Reserva
- `usuario` (ForeignKey → User)
- `espaco` (ForeignKey → Espaco)
- `data` (DateField)
- `hora_inicio` (TimeField)
- `hora_fim` (TimeField)
- `descricao` (CharField, opcional)

---

## 🔒 Validações Implementadas

1. **Conflito de Horários:** Impede reservas sobrepostas no mesmo espaço e data
2. **Datas Passadas:** Não permite agendamentos retroativos
3. **Horário Válido:** hora_inicio deve ser anterior a hora_fim
4. **Integridade:** Índices de banco de dados para performance

---

## 📞 Próximas Fases

- **Frontend:** Criar templates HTML/CSS e formulários
- **Views:** Desenvolver lógica de visualização e CRUD
- **Autenticação:** Configurar permissões por papel (Aluno/Professor/Admin)

---

**Desenvolvido com Django 6.0 | Python 3.x**
