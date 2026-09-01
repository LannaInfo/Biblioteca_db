import sqlite3

conn = sqlite3.connect("Biblioteca.db")
conn.executemany("INSERT INTO usuarios(nome) VALUES(?)",
                 [("Carlos",), ("Mateus",), ("Ana Laura",),])
conn.commit()