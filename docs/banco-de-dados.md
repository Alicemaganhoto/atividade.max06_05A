# Banco de Dados

O sistema utiliza SQLite para armazenamento das informações.

---

# Tabela Cinema

```sql
CREATE TABLE cinema (
    idCinema INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    endereco TEXT NOT NULL,
    capacidadePublico INTEGER NOT NULL
);

# Tabela Filme

SQL
CREATE TABLE filme (
    idFilme INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    genero TEXT NOT NULL,
    diretor TEXT NOT NULL,
    elenco TEXT NOT NULL,
    duracao INTEGER NOT NULL
);
# Tabela Sessao

SQL
CREATE TABLE sessao (
    idSessao INTEGER PRIMARY KEY AUTOINCREMENT,
    horario TEXT NOT NULL,
    data TEXT NOT NULL,
    publico INTEGER,
    idCinema INTEGER,
    idFilme INTEGER,
    
    FOREIGN KEY(idCinema) REFERENCES cinema(idCinema),
    FOREIGN KEY(idFilme) REFERENCES filme(idFilme)
);
