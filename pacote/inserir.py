import sqlite3
from database import conectar

def adicionar(nome,idade,email,telefone):
    comando = ("INSERT INTO user (nome, idade, email, telefone) VALUES (?,?,?,?)")
    with conectar() as conexao:

        cursor = conexao.cursor()
        cursor.execute(comando,(nome,idade,email,telefone))
    
        conexao.commit()
    
    return "Adicionado com sucesso"

