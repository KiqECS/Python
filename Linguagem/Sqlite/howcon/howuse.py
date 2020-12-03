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

#Recebe informações do User
def info():
    i_nome = input("Digite seu nome: ")
    i_idade = input("Digite a sua idade: ")   
    return i_nome,i_idade

#Insere itens dentro da tabela criada anteriormente 
def insert_db(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print("Adicionado com sucesso")
    except Error as ex:
        print("Não adicionado")
        print(ex)

def insert():
    i_nome,i_idade = info()
    #Script SQL para que insere as infomações na tebela
    s_insert_sql = ("insert into pessoa (nome,idade) values('{}','{}')").format(i_nome,i_idade)
    insert_db(c_con_db,s_insert_sql)

def delete_db(conexao,sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print("Removido com sucesso")
    except Error as ex:
        print("Não Removido")
        print(ex)

#Def para deletar do DB
def delete(table,id):
    #Script sql para deletar
    s_delete_sql = ("DELETE FROM {} WHERE id = {}").format(table,id)
    #Chamada da função de delete
    delete_db(c_con_db,s_delete_sql)

def select_db(conexao,sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        all_db = c.fetchall()
        return all_db
    except Error as ex:
        print("Erro na entrega")
        print(ex)

#Script para seleção 
s_select_sql = "SELECT * FROM pessoa"

#Def para mostrar as informações na tela
def show_select():
    ret_select_db=select_db(c_con_db,s_select_sql)
    for r in ret_select_db:
        print(r)

#IMPORTANTE!! 
#Fechamento da DB no final o processo
c_con_db.close()