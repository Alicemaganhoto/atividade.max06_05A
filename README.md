# Sistema de Rede de Cinemas

# Levantamento de Requisitos e Regras de Negócio

## Requisitos Funcionais

1. Cadastrar cinemas da rede.

2. Cadastrar filmes em exibição.

3. Cadastrar sessões dos filmes.

4. Consultar informações de filmes, elenco, diretores e gêneros.

5. Registrar público de cada sessão.

6. Consultar total de público por sessão.

7. Consultar total de público por filme.

8. Consultar total de público por cinema.

---

## Regras de Negócio

1. Um cinema pode possuir várias sessões.

2. Um filme pode estar em cartaz em diferentes cinemas.

3. Toda sessão deve estar vinculada a um único filme.

4. O horário das sessões deve respeitar a duração do filme e intervalo entre exibições.

5. O público registrado em uma sessão não pode ultrapassar a capacidade do cinema.

6. O registro de público deve ser feito diariamente.

7. Filmes devem possuir pelo menos um gênero cadastrado.

---

# Diagrama de Casos de Uso (Visão Geral)

## Atores

- Administrador
- Funcionário
- Espectador

## Casos de Uso

### Administrador

- Gerenciar cinemas
- Gerenciar funcionários
- Consultar relatórios

### Funcionário

- Cadastrar filme
- Cadastrar sessão
- Registrar público

### Espectador

- Consultar filmes
- Consultar sessões
- Consultar informações do filme

<img width="411" height="700" alt="image" src="https://github.com/user-attachments/assets/e95d255c-d74a-4e19-b712-446e3351798d" />

---

# Diagrama de Classes do Domínio

## Cinema

- idCinema
- nome
- endereco
- capacidadePublico

## Filme

- idFilme
- titulo
- genero
- diretor
- elenco
- duracao

## Sessao

- idSessao
- horario
- data
- publico

## Relacionamentos

- Um Cinema possui várias Sessões.
- Um Filme possui várias Sessões.
- Uma Sessão pertence a um Cinema.
- Uma Sessão pertence a um Filme.

<img width="401" height="346" alt="image" src="https://github.com/user-attachments/assets/f61b1cba-f19f-4602-a9c6-24b535a1f590" />

---

# Diagramas de Atividade

## Cadastro de Filme

Início → Preencher dados do filme → Validar informações → Salvar filme → Fim

<img width="302" height="367" alt="image" src="https://github.com/user-attachments/assets/26ca2ad8-0223-4c0a-9838-501024d09bd6" />

## Cadastro de Sessão

Início → Selecionar cinema → Selecionar filme → Informar horário → Validar conflito de horário → Salvar sessão → Fim

<img width="300" height="474" alt="image" src="https://github.com/user-attachments/assets/3f41dda6-e2a4-43ae-9709-d85b25c270c8" />

## Registro de Público

Início → Selecionar sessão → Informar quantidade de público → Validar capacidade → Salvar registro → Fim

<img width="428" height="477" alt="image" src="https://github.com/user-attachments/assets/d9fc7dfd-0d50-4816-b2d9-e07611231048" />

---

# Diagramas de Sequência

## Cadastro de Filme

View → Controller: enviarDadosFilme()

Controller → Service: cadastrarFilme()

Service → Repository: salvarFilme()

Repository → SQLite: INSERT filme

SQLite → Repository: confirmação

Repository → Service: sucesso

Service → Controller: retorno

Controller → View: mensagem de sucesso

<img width="636" height="432" alt="image" src="https://github.com/user-attachments/assets/6cbd1de5-62ff-453c-a4f8-cdaacd0579ef" />


---

## Registro de Público

View → Controller: registrarPublico()

Controller → Service: validarCapacidade()

Service → Repository: buscarSessao()

Repository → SQLite: SELECT sessão

SQLite → Repository: dados sessão

Repository → Service: retorno

Service → Repository: atualizarPublico()

Repository → SQLite: UPDATE sessão

SQLite → Repository: confirmação

Repository → Service: sucesso

Service → Controller: retorno

Controller → View: mensagem de sucesso

<img width="636" height="500" alt="image" src="https://github.com/user-attachments/assets/6262fdb8-0268-42cd-a019-d3cb46381f8a" />

---

# Implementação

## Caso de Uso Implementado

Cadastro de Filmes.

# Arquitetura do Sistema

O sistema foi desenvolvido utilizando arquitetura em camadas, seguindo o padrão MVC junto das camadas Service e Repository, garantindo melhor organização, manutenção e separação de responsabilidades.

## Camadas da Arquitetura

### View
Responsável pela interação com o usuário, recebendo entradas e exibindo informações do sistema.

Exemplos:
- Tela de cadastro de filmes
- Tela de sessões
- Tela de relatórios

---

### Controller
Responsável por receber as requisições da View e encaminhar para as regras de negócio.

Funções:
- Receber dados dos formulários
- Validar entradas básicas
- Chamar os Services

---

### Service
Responsável pelas regras de negócio da aplicação.

Funções:
- Validar capacidade do cinema
- Validar horários de sessões
- Processar regras do sistema

---

### Repository
Responsável pela persistência dos dados no banco SQLite.

Funções:
- Salvar registros
- Atualizar informações
- Buscar dados no banco

---

### Model
Representa as entidades do sistema.

Exemplos:
- Cinema
- Filme
- Sessao
- Administrador
- Funcionario

---

### Database
Responsável pela conexão com o banco SQLite.

Funções:
- Abrir conexão
- Executar comandos SQL
- Gerenciar persistência

---

# Fluxo da Arquitetura

View → Controller → Service → Repository → SQLite

SQLite → Repository → Service → Controller → View
