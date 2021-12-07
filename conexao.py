import mysql.connector


def criar_conexao(localhost,usuario,senha,banco):
    return mysql.connector.connect(host = localhost, user = usuario, password = senha, database = banco)

def fechar_conexao(con):
    return  con.close()    