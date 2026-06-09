import sqlite3
from pacote.database import conectar

def buscar(dados,escolha):
    comando_id = ('SELECT * FROM user WHERE id = (?)')
    comando_email = ('SELECT * FROM user WHERE email = (?)')

    with conectar() as conexao:
        cursor = conexao.cursor()
        if escolha == 1:
            cursor.execute(comando_id,(dados,))
            resultado = cursor.fetchall()
            print(resultado)

        elif escolha == 2:
            cursor.execute(comando_email,(dados,))
            resultado = cursor.fetchall()
            print(resultado)
            
        conexao.commit()
