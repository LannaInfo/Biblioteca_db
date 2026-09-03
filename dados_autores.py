import sqlite3

conn = sqlite3.connect("Biblioteca.db")

conn.execute('DROP TABLE  IF EXISTS Editora')

#criar a tabela Editora
conn.execute('CREATE TABLE Editora (id INTEGER PRIMARY KEY AUTOINCREMENT, nome  TEXT NOT NULL)')

conn.executemany("INSERT INTO Editora (nome) VALUES(?)",
                 [("Malevola",), ("Dalmata",),])


conn.commit()
