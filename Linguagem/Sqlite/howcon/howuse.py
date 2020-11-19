import sqlite3
from sqlite3 import Error

#Cria a Conexão com a DB
def con_db(caminho):
    con = None
    try:
        con = sqlite3.connect(caminho)
        print("Conexão bem sucedida")
    except Error as ex:
        print("Erro na conexão")
        print(ex)
    return con

c_con_db = con_db("/home/kiq/LearnWhatever/Python/Linguagem/Sqlite/db1.db") #Caminho da DB

#Cria a Tabela
def create_t(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        print("Tabela Criada")
    except Error as ex:
        print("Tabela não criada")
        print(ex)

#Script SQL para a criação da tabela
s_create_sql = """Create table pessoa(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome varchar(50),
            idade INTEGER
        )"""

#Insere itens dentro da tabela criada anteriormente 
def ins_db(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print("Adicionado com sucesso")
    except Error as ex:
        print("Não adicionado")
        print(ex)

#Recebe informações do User
def info():
    i_nome = input("Digite seu nome: ")
    i_idade = input("Digite a sua idade: ")   
    return i_nome,i_idade

i_nome,i_idade = info()

#Script SQL para que insere as infomções na tebela
s_insert_sql = ("insert into pessoa (nome,idade) values('{}','{}')").format(i_nome,i_idade)

def delete_db(conexao,sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print("Removido com sucesso")
    except Error as ex:
        print("Não Removido")
        print(ex)

s_delete_db = "DELETE FROM pessoa WHERE id = 2"

ins_db(c_con_db,s_insert_sql)

#IMPORTANTE!! 
#Fechamento da DB no final o processo
c_con_db.close()