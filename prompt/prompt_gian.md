Aja como um Engenheiro de Software Sênior especialista em Python/Django, com foco em boas práticas de arquitetura, código limpo e projetos prontos para produção.

Sou o responsável pelo Backend e pela Infraestrutura base de um projeto acadêmico chamado "Sistema de Reserva de Salas e Laboratórios". Preciso que você gere um guia completo de setup e o código base inicial do projeto, seguindo boas práticas do mercado.

DIRETRIZES DE SAÍDA:

Forneça respostas diretas, organizadas em Markdown.

Use blocos de código (```python, ```bash) para todos os scripts e comandos.

Seja conciso nas explicações, focando no "porquê" técnico. Sem introduções longas.

Para este escopo inicial, considere o banco de dados padrão (SQLite).

1. Setup do Ambiente e Projeto
Forneça um passo a passo em blocos de código com comandos de terminal para:

Criar um ambiente virtual (venv) nativo do Python.

Ativar o ambiente virtual (mostre comandos para Windows PowerShell e Linux/Mac bash).

Instalar o Django e gerar o arquivo requirements.txt.

Criar um arquivo .gitignore padrão para projetos Django.

Criar um novo projeto chamado core.

Criar uma app chamada reservas.

Executar as migrações iniciais e o servidor pela primeira vez.

2. Modelagem de Dados (models.py)
Crie modelos Django com boas práticas para a app reservas:

Modelo: Espaco -> nome (CharField), tipo (usar TextChoices: Sala / Laboratório), capacidade (PositiveIntegerField), possui_computadores (BooleanField).

Modelo: Reserva -> usuario (ForeignKey para User padrão do Django), espaco (ForeignKey para Espaco), data (DateField), hora_inicio (TimeField), hora_fim (TimeField).

Regras de negócio obrigatórias no modelo Reserva:

Validar que hora_inicio < hora_fim.

Impedir agendamentos em datas no passado.

Impedir sobreposição de horários para o mesmo espaço na mesma data.

Implemente o método clean() fazendo uso de Q objects para verificar a interseção de horários. Inclua a exclusão do próprio registro (self.pk) em caso de update e lance um ValidationError com mensagem amigável. Explique brevemente, em texto, a lógica booleana dessa interseção.

Estrutura dos Modelos: Inclua __str__, classe Meta (com ordering), e índices de banco de dados (indexes) nas colunas mais consultadas (como data e espaço) visando performance.

3. Configurações Base (settings.py)
Mostre exatamente o que deve ser alterado/adicionado no settings.py:

Registro da app reservas.

Configuração rigorosa de arquivos estáticos (STATIC_URL, STATIC_ROOT, STATICFILES_DIRS).

Internacionalização: LANGUAGE_CODE = 'pt-br' e TIME_ZONE = 'America/Sao_Paulo'.

4. Painel Administrativo (admin.py)
Registre os modelos configurando uma interface rica para testes de CRUD da equipe:

EspacoAdmin: Configure list_display, list_filter e search_fields.

ReservaAdmin: Configure list_display, list_filter, search_fields, ordering e autocomplete_fields (se aplicável).

5. Teste Unitário Essencial (tests.py)
Crie um teste unitário simples e direto no tests.py da app reservas que tente criar uma reserva encavalada com outra existente para provar que o método clean() levanta o ValidationError corretamente.