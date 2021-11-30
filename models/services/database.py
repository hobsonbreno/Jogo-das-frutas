import pyodbc

server = ''
database =''
username = 'Admin'
password = '007hb'
cnxn = cnxn.pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=+server+';DATABASE='+database+';UID='+username+';PWD='+password)