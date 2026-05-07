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
