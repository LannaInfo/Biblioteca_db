import sqlite3

conn = sqlite3.connect("Biblioteca.db")

conn.execute('DROP TABLE  IF EXISTS Emprestimos')

#criar a tabela Editora
conn.execute('CREATE TABLE Emprestimos (id INTEGER PRIMARY KEY AUTOINCREMENT, nome  TEXT NOT NULL)')

conn.executemany("INSERT INTO  (nome) VALUES(?)",
                 [("Malevola",), ("Dalmata",),])


conn.commit()
