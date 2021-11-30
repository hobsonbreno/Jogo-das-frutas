import services.database as db;


def incluir(cliente):
    count = cursor.execute("""
    INSERT INTO Cliente(cliNome,cliDeposito,cliAposta)
    VALUES(?,?,?)""",
    cliente.nome, cliente.deposito, cliente.aposta).rowcount
    cnxn.commit()
}