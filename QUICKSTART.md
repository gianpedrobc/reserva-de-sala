# 🎯 Quick Start - Servidor Django

## ⚡ Em 3 Passos

### Passo 1: Ativar Ambiente Virtual
```powershell
.\venv\Scripts\Activate.ps1
```

### Passo 2: Rodar Servidor
```bash
python manage.py runserver
```

### Passo 3: Acessar
- **App:** http://localhost:8000/
- **Admin:** http://localhost:8000/admin/
  - User: `admin`
  - Pass: `admin123`

---

## 🔧 Comandos Úteis

### Criar migrações após modificar models.py
```bash
python manage.py makemigrations
python manage.py migrate
```

### Rodar testes
```bash
python manage.py test reservas
```

### Shell interativo Django
```bash
python manage.py shell
```

### Criar novo super usuário
```bash
python manage.py createsuperuser
```

---

## 📱 Acessar de Outros Computadores

No lugar de `localhost:8000`, use:
```bash
python manage.py runserver 0.0.0.0:8000
```

Acesse com: `http://SEU_IP:8000/`

---

**Pronto para desenvolver! 🚀**
