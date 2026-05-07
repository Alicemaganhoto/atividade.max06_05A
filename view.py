# FilmeView.py

Python
from controller.FilmeController import FilmeController
from model.Filme import Filme

class FilmeView:

    def cadastrarFilme(self):

        filme = Filme(
            1,
            "Vingadores",
            "Acao",
            "Marvel",
            "Robert Downey Jr",
            180
        )

        controller = FilmeController()

        controller.cadastrarFilme(filme)

---

# SessaoView.py

Python
from controller.SessaoController import SessaoController
from model.Sessao import Sessao

class SessaoView:

    def registrarPublico(self):

        sessao = Sessao(
            1,
            "20:00",
            "06/05/2026",
            50
        )

        controller = SessaoController()

        controller.registrarPublico(
            sessao,
            20,
            100
        )
