import pyodbc

server = ''
database =''
username = ''
password = ' '
cnxn = cnxn.pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=+server+';DATABASE='+database+';UID='+username+';PWD='+password)
                           
                           
                            
import mysql.connector


def criar_conexao(localhost,usuario,senha,banco):
    return mysql.connector.connect(host = localhost, user = usuario, password = senha, database = banco)

def fechar_conexao(con):
    return  con.close()    