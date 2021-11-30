import services.database as db;


def incluir(cliente):
    count = cursor.execute("""
    INSERT INTO Cliente(cliNome,cliFrutas,cliDeposito)
    VALUES(?,?,?)""",
    cliente.nome, cliente.frutas, cliente.deposito).rowcount
    cnxn.commit()
}