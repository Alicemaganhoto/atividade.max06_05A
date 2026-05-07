# Arquitetura do Sistema

O sistema utiliza arquitetura em camadas baseada no padrão MVC juntamente com as camadas Service e Repository.

---

# Estrutura das Camadas

## View
Responsável pela interação com o usuário.

Exemplos:
- Cadastro de filmes
- Cadastro de sessões
- Relatórios

---

## Controller
Responsável por receber as ações da View e encaminhar para os serviços.

Funções:
- Receber requisições
- Validar entradas básicas
- Chamar Services

---

## Service
Responsável pelas regras de negócio do sistema.

Funções:
- Validar capacidade do cinema
- Validar horários de sessões
- Processar regras do sistema

---

## Repository
Responsável pela persistência dos dados.

Funções:
- Salvar registros
- Buscar dados
- Atualizar informações

---

## Model
Representa as entidades do sistema.

Entidades:
- Cinema
- Filme
- Sessao
- Administrador
- Funcionario

---

## Database
Responsável pela conexão com o banco SQLite.

---

# Fluxo da Arquitetura

View → Controller → Service → Repository → SQLite
