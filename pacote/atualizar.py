import sqlite3
from pacote.database import conectar

def alterar(id, campo, valor):

     
    campos_permitidos = ["nome", "idade", "email", "telefone"]

    if campo not in campos_permitidos:
        print("Campo inválido")
        return
    
    query = f"UPDATE user SET {campo} = ? WHERE id = ?"
    
    with conectar() as conexao:
        cursor = conexao.cursor()
        cursor.execute(query,(valor,id))

        conexao.commit()    
