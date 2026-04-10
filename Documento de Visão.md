# DOCUMENTO DE VISÃO E REQUISITOS

**Projeto:** Sistema de Reserva de Salas e Laboratórios  
**Contexto:** Projeto Acadêmico - Engenharia de Software | Licenciatura em Ciências da Computação  
**Data:** 10 de Abril de 2026

---

## 1. OBJETIVOO objetivo deste documento é definir, de forma clara e não ambígua, as características, o escopo, os requisitos e a arquitetura inicial do "Sistema de Reserva de Salas e Laboratórios". Este artefato serve como contrato de escopo entre a equipe de desenvolvimento e os stakeholders (professores, alunos e coordenação), garantindo que a solução construída atenda às necessidades reais da instituição de ensino.

---

## 2. VISÃO GERAL DO CONTEXTONo ambiente educacional contemporâneo, a otimização da infraestrutura física é essencial. A instituição conta com diversos espaços compartilhados (salas de aula, laboratórios de informática, laboratórios específicos) que são utilizados diariamente por diferentes turmas, docentes e monitores. Atualmente, a gestão do uso desses espaços carece de um processo centralizado e transparente, dependendo de verificações presenciais ou comunicações informais.

---

## 3. MAPEAMENTO DOS PROBLEMASA ausência de um sistema automatizado gera os seguintes impactos negativos na rotina acadêmica:

- **Conflitos de Alocação:** Ocorrência frequente de double-booking (duas turmas ou grupos tentando utilizar o mesmo espaço simultaneamente).
- **Falta de Visibilidade:** Alunos e professores não têm como consultar remotamente e em tempo real quais laboratórios estão livres para estudo ou pesquisa.
- **Desperdício de Tempo Produtivo:** Necessidade de deslocamento físico apenas para verificar a disponibilidade de uma sala ou procurar o responsável pelas chaves.
- **Subutilização da Infraestrutura:** Espaços ociosos não são aproveitados por falta de comunicação sobre sua vacância.

---

## 4. VISÃO GERAL DA SOLUÇÃO PROPOSTAA solução proposta é o desenvolvimento de uma aplicação web (com interface responsiva para mobile) focada na gestão e reserva de espaços físicos. O sistema consistirá em um CRUD clássico e robusto, automatizando o controle de acesso e o agendamento. Através do sistema, a comunidade acadêmica poderá visualizar a grade de ocupação, solicitar horários e receber confirmações automáticas, enquanto o motor do sistema garante a prevenção sistêmica de qualquer conflito de horários.

---

## 5. ATORES DO SISTEMA- **Usuário Comum (Aluno/Professor):** Pode visualizar a disponibilidade de espaços, realizar reservas para si e cancelar suas próprias reservas.
- **Administrador (TI/Coordenação):** Possui privilégios totais. Pode cadastrar novos espaços, gerenciar usuários, visualizar todas as reservas do sistema e cancelar reservas de terceiros, se necessário.

---

## 6. REQUISITOS FUNCIONAIS (RF)

Compreendem as funcionalidades diretas que o sistema deve prover aos usuários.

| ID | Descrição do Requisito | Complexidade | Criticidade | Dependência |
|:---|:---|:---|:---|:---|
| RF01 | O sistema deve permitir a autenticação e autorização de usuários (Login/Logout). | Média | Alta | Nenhuma |
| RF02 | O sistema deve permitir o CRUD de Usuários pelos administradores. | Baixa | Média | RF01 |
| RF03 | O sistema deve permitir o CRUD de Espaços (Salas e Labs), incluindo nome, capacidade e infraestrutura. | Baixa | Alta | RF01 |
| RF04 | O sistema deve disponibilizar um painel para visualização de espaços disponíveis, com filtros por data. | Média | Alta | RF03 |
| RF05 | O sistema deve permitir que um usuário autenticado realize a solicitação de reserva de um espaço. | Média | Alta | RF01, RF04 |
| RF06 | O sistema deve exibir detalhes das reservas ativas vinculadas ao usuário logado. | Baixa | Alta | RF05 |
| RF07 | O sistema deve permitir que o usuário cancele uma reserva previamente feita por ele mesmo. | Baixa | Média | RF05 |

---

## 7. REQUISITOS NÃO FUNCIONAIS (RNF)

Definem os atributos de qualidade, restrições e premissas arquiteturais.

| ID | Descrição do Requisito | Complexidade | Criticidade | Dependência |
|:---|:---|:---|:---|:---|
| RNF01 | Interface: O sistema deve ser responsivo (Web/Mobile) utilizando HTML5, CSS3 e boas práticas de UI/UX. | Média | Alta | Nenhuma |
| RNF02 | Tecnologia Base: O backend deve ser construído utilizando o framework Django (Python), aproveitando seu ORM e painel administrativo nativo. | Baixa | Alta | Nenhuma |
| RNF03 | Persistência: Os dados devem ser persistidos em um banco de dados relacional (ex: PostgreSQL ou SQLite para desenvolvimento). | Baixa | Alta | RNF02 |
| RNF04 | Segurança: As senhas dos usuários devem ser armazenadas com criptografia (hash) e rotas sensíveis devem exigir autenticação. | Média | Alta | RNF02 |

---

## 8. REGRAS DE NEGÓCIO (RN)RN01 - Prevenção de Conflitos: O sistema não pode, em nenhuma hipótese, salvar uma nova reserva se a Data e o intervalo de Tempo (Hora Início e Hora Fim) coincidirem ou se sobrepuserem a uma reserva já existente e ativa para o mesmo Espaço.RN02 - Restrição de Cancelamento: Um usuário comum só pode cancelar reservas atreladas ao seu próprio ID. Apenas um Administrador pode cancelar reservas de terceiros.RN03 - Reservas Retroativas: O sistema não deve permitir o agendamento de reservas para datas e horários que já passaram em relação ao horário atual do servidor.9. MODELAGEM DO SISTEMA9.1. Diagrama de Casos de Uso(Copie o código abaixo e cole no site PlantText para gerar a imagem e colocar no seu documento)Snippet de código@startuml
left to right direction
skinparam packageStyle rectangle

actor "Usuário\n(Aluno/Professor)" as user
actor "Administrador\n(Staff/TI)" as admin

package "Sistema de Reservas" {
  usecase "Realizar Login" as UC1
  usecase "Consultar Disponibilidade" as UC2
  usecase "Realizar Reserva" as UC3
  usecase "Cancelar Própria Reserva" as UC4
  usecase "Gerenciar Espaços (CRUD)" as UC5
  usecase "Gerenciar Usuários" as UC6
}

user --> UC1
user --> UC2
user --> UC3
user --> UC4

admin --> UC1
admin --> UC2
admin --> UC5
admin --> UC6

UC3 ..> UC1 : <<include>>
UC4 ..> UC1 : <<include>>
UC5 ..> UC1 : <<include>>
UC6 ..> UC1 : <<include>>
@enduml
```

### 9.2. Descrição Textual dos Casos de Uso (Detalhamento)

#### Caso de Uso: Realizar Reserva (UC3)

**Ator Principal:** Usuário (Aluno/Professor)

**Pré-condição:** O usuário deve estar autenticado no sistema (UC1)

**Fluxo Principal (Caminho Feliz):**
1. O usuário acessa a tela de agendamentos.
2. O usuário seleciona o Espaço desejado, a Data, a Hora de Início e a Hora de Término.
3. O usuário clica em "Confirmar Reserva".
4. O sistema valida os dados recebidos.
5. O sistema executa a checagem de conflitos (RN01) e verifica que o horário está livre.
6. O sistema registra a reserva no banco de dados com status "Ativa".
7. O sistema exibe uma mensagem de sucesso na tela para o usuário.

**Fluxo de Exceção (Conflito de Horário):**
- No passo 5, se o sistema detectar que já existe uma reserva para aquele espaço no mesmo horário, a operação é interrompida.
- O sistema não salva a reserva e exibe a mensagem de erro: *"Este espaço já está reservado para o horário selecionado. Por favor, escolha outro horário."*

### 9.3. Diagrama de Classes

```plantuml@startuml
skinparam classAttributeIconSize 0

class Usuario {
  - id: Integer
  - nome: String
  - email: String
  - matricula: String
  - is_staff: Boolean
  + fazer_login()
}

class Espaco {
  - id: Integer
  - nome: String
  - tipo: String
  - capacidade: Integer
  + verificar_disponibilidade(data, hora_inicio, hora_fim): Boolean
}

class Reserva {
  - id: Integer
  - data: Date
  - hora_inicio: Time
  - hora_fim: Time
  - status: String
  - motivo: String
  + clean() // Método do Django para validar RN01
  + save()
}

Usuario "1" -- "0..*" Reserva : "possui >"
Espaco "1" -- "0..*" Reserva : "recebe >"

@enduml
```

---

**Fim do Documento de Visão**