import sqlite3

conn = sqlite3.connect("Biblioteca.db")

conn.execute('DROP TABLE  IF EXISTS usuarios')

#criar a tabela usuarios
conn.execute('CREATE TABLE usuarios (id INTEGER PRIMARY KEY AUTOINCREMENT, nome  TEXT NOT NULL)')

conn.executemany("INSERT INTO usuarios(nome) VALUES(?)",
                 [("Carlos",), ("Mateus",), ("Ana Laura",),])


conn.commit()




