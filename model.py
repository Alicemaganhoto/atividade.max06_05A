# Cinema.py

Python
class Cinema:

    def __init__(self, idCinema, nome, endereco, capacidadePublico):
        self.idCinema = idCinema
        self.nome = nome
        self.endereco = endereco
        self.capacidadePublico = capacidadePublico
Filme.py
Python
class Filme:

    def __init__(self, idFilme, titulo, genero, diretor, elenco, duracao):
        self.idFilme = idFilme
        self.titulo = titulo
        self.genero = genero
        self.diretor = diretor
        self.elenco = elenco
        self.duracao = duracao

---

# Sessao.py

Python
class Sessao:

    def __init__(self, idSessao, horario, data, publico):
        self.idSessao = idSessao
        self.horario = horario
        self.data = data
        self.publico = publico
Administrador.py
Python
class Administrador:

    def __init__(self, idAdministrador, nome, login, senha):
        self.idAdministrador = idAdministrador
        self.nome = nome
        self.login = login
        self.senha = senha
Funcionario.py
Python
class Funcionario:

    def __init__(self, idFuncionario, nome, login, senha):
        self.idFuncionario = idFuncionario
        self.nome = nome
        self.login = login
        self.senha = senha
