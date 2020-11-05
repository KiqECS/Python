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
    
c_sql = """Create table pessoa(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome varchar(50),
            idade INTEGER
        )"""

def insdb(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print("Adicionado com sucesso")
    except Error as ex:
        print("Não adicionado")
        print(ex)


i_nome = input("Digite seu nome: ")
i_idade = input("Digite a sua idade: ")

i_sql = "insert into pessoa (nome,idade) values('"+i_nome+"','"+i_idade+"')" 

insdb(c_condb,i_sql)
c_condb.close()

