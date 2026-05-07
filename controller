# FilmeController.py

Python
from service.FilmeService import FilmeService

class FilmeController:

    def __init__(self):
        self.service = FilmeService()

    def cadastrarFilme(self, filme):

        self.service.cadastrarFilme(filme)

---

# SessaoController.py

Python
from service.SessaoService import SessaoService

class SessaoController:

    def __init__(self):
        self.service = SessaoService()

    def cadastrarSessao(self, sessao):

        self.service.cadastrarSessao(sessao)

    def registrarPublico(self, sessao, quantidade, capacidadeCinema):

        self.service.registrarPublico(
            sessao,
            quantidade,
            capacidadeCinema
        )
