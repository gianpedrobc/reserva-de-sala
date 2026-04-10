# PLANO DE DESENVOLVIMENTO ÁGIL (4 PESSOAS)

**Projeto:** Sistema de Reserva de Salas e Laboratórios  
**Metodologia:** Ágil (Sprints de 1 a 2 semanas)

---

## 1. DEFINIÇÃO DOS PAPÉIS (A EQUIPE)

A divisão não significa que um não possa ajudar o outro, mas define quem é o responsável principal pela entrega daquela área.

### Membro 1: Gian (Arquitetura Backend & Infraestrutura)

- **Foco:** Estrutura base do projeto.
- **Responsabilidades:** Configuração inicial do Django (settings.py), criação dos models.py (banco de dados), mapeamento de rotas principais (urls.py) e preparação do ambiente para um eventual deploy (ex: instâncias na AWS).

### Membro 2: Desenvolvedor Frontend (UI/UX)

- **Foco:** O que o usuário vê.
- **Responsabilidades:** Criação das telas (HTML/CSS) focando em responsividade (mobile-first), integração dos templates do Django e design do painel de visualização de horários livres.

### Membro 3: Desenvolvedor de Regras de Negócio (Views & Lógica)

- **Foco:** O motor do sistema.
- **Responsabilidades:** Escrever as views.py, processar os formulários de reserva e, principalmente, programar a trava de segurança que impede conflitos de horário no momento do agendamento.

### Membro 4: Autenticação, Admin & Qualidade (QA)

- **Foco:** Controle de acesso e testes.
- **Responsabilidades:** Configurar os grupos de permissão (Aluno/Professor/Admin), customizar o painel nativo do Django Admin para facilitar o CRUD de salas, e testar intensamente o sistema (tentar "quebrar" os bloqueios de horário).

---

## 2. ROADMAP DE DESENVOLVIMENTO (SPRINTS)

O projeto pode ser dividido em 4 Sprints principais. Cada final de Sprint deve gerar uma versão testável do sistema.

---

### Sprint 1: Fundação e Autenticação (A Base)

**Objetivo:** Ter o sistema rodando, com o banco de dados criado e os usuários conseguindo fazer login.

| Tarefa | Responsável Principal | O que entregar ao final do Sprint |
|:---|:---|:---|
| Setup Inicial: Criar projeto Django e repositório no GitHub. | Gian | Projeto rodando sem erros no localhost. |
| Modelagem: Escrever o arquivo models.py com as classes Usuario, Espaco e Reserva. | Gian | Tabelas criadas no banco (makemigrations/migrate). |
| Interface Base: Criar o template HTML base com o menu de navegação e rodapé. | Membro 2 | Arquivo base.html pronto e responsivo. |
| Autenticação: Configurar Login/Logout e acessos básicos no Django. | Membro 4 | Telas de login e registro funcionando. |

---

### Sprint 2: Cadastros e Painel Administrativo (O CRUD)

**Objetivo:** Permitir que administradores cadastrem as salas/laboratórios e que os usuários vejam essas salas.

| Tarefa | Responsável Principal | O que entregar ao final do Sprint |
|:---|:---|:---|
| Painel Admin: Registrar os models no admin.py e customizar a visualização. | Membro 4 | CRUD completo e fácil de usar via Django Admin. |
| Listagem de Espaços: Criar a lógica (views.py) para puxar as salas do banco. | Membro 3 | View que envia os dados das salas para o HTML. |
| Página de Salas: Construir a tela que mostra a lista de laboratórios com fotos/descrições. | Membro 2 | Tela bonita listando tudo o que está cadastrado. |
| Infraestrutura: Garantir que imagens e arquivos estáticos estão carregando corretamente. | Gian | Servidor estático (STATIC_URL etc.) configurado. |

---

### Sprint 3: O Motor de Reservas (O Coração do Projeto)

**Objetivo:** Fazer o agendamento funcionar com a regra que impede horários encavalados.

| Tarefa | Responsável Principal | O que entregar ao final do Sprint |
|:---|:---|:---|
| Regra de Negócio (Conflitos): Lógica que cruza data/hora escolhida com reservas ativas. | Membro 3 | O backend deve recusar reservas inválidas de forma segura. |
| Formulário de Reserva: Criar o form em Django e a tela HTML para o usuário escolher o horário. | Membro 2 | Interface clara com calendário e seleção de horário. |
| Validação no Modelo: Adicionar o método clean() no models.py para dupla proteção. | Gian | Banco de dados blindado contra sobreposições. |
| Meus Agendamentos: Tela onde o usuário vê suas reservas e pode clicar em "Cancelar". | Membro 4 / Membro 3 | Lista individual de reservas funcionando. |

---

### Sprint 4: Testes, Polimento e Deploy (A Entrega)

**Objetivo:** Encontrar falhas estruturais, deixar o sistema bonito e prepará-lo para a apresentação ao professor.

| Tarefa | Responsável Principal | O que entregar ao final do Sprint |
|:---|:---|:---|
| Bateria de Testes: Tentar fazer reservas no passado, com horários absurdos ou sem login. | Membro 4 | Relatório de bugs encontrados e corrigidos. |
| Refinamento de UI: Ajustar cores, botões, espaçamentos e testar no celular. | Membro 2 | Interface final polida e profissional. |
| Fechamento de Código: Revisar views, limpar código não utilizado, documentar funções. | Membro 3 | Código limpo e fácil de apresentar/explicar. |
| Deploy (Opcional/Extra): Subir o sistema para uma instância real (AWS EC2, Heroku, Render). | Gian | Link público do sistema funcionando na nuvem. |

---

**Fim do Plano de Desenvolvimento**