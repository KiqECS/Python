import sqlite3
from sqlite3 import Error

def condb(caminho):
    con = None
    try:
        con = sqlite3.connect(caminho)
        print("Conexão bem sucedida")
    except Error as ex:
        print("Erro na conexão")
        print(ex)
    return con

c_condb = condb("/home/kiq/LearnWhatever/Python/Sqlite/db1.db")

def createt(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        print("Tabela Criada")
    except Error as ex:
        print("Tabela não criada")
        print(ex)
    
q_sql = """Create table pessoa(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome varchar(50),
            idade INTEGER
        )"""

createt(c_condb,q_sql)
c_condb.close()

