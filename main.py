from view.FilmeView import FilmeView
from view.SessaoView import SessaoView

print("=== CADASTRO DE FILME ===")

filmeView = FilmeView()
filmeView.cadastrarFilme()

print("\n=== REGISTRO DE PUBLICO ===")

sessaoView = SessaoView()
sessaoView.registrarPublico()
