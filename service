# FilmeService.py

Python
from repository.FilmeRepository import FilmeRepository

class FilmeService:

    def __init__(self):
        self.repository = FilmeRepository()

    def cadastrarFilme(self, filme):

        if filme.titulo == "":
            print("Erro: titulo invalido")
            return

        self.repository.salvarFilme(filme)

---

# SessaoService.py

Python
from repository.SessaoRepository import SessaoRepository

class SessaoService:

    def __init__(self):
        self.repository = SessaoRepository()

    def cadastrarSessao(self, sessao):

        self.repository.salvarSessao(sessao)

    def registrarPublico(self, sessao, quantidade, capacidadeCinema):

        if sessao.publico + quantidade > capacidadeCinema:

            print("Erro: capacidade excedida")
            return

        self.repository.atualizarPublico(sessao, quantidade)
