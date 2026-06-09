import sqlite3 
from pacote.database import conectar

def delete(dados,escolha):
    comando_id = ('DELETE FROM user WHERE id = (?)')
    comando_email = ('DELETE FROM user WHERE email = (?)')

    with conectar() as conexao:
        cursor = conexao.cursor()
        if escolha == 1:
            cursor.execute(comando_id,(dados,))
        else:
            cursor.execute(comando_email,(dados,))
            
        conexao.commit()

    print("Deletado com sucesso")
    
