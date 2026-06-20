
def linha(tam=44):
    return "-" * tam


def titulo(texto):
    print(linha())
    print(texto.center(40))
    print(linha())


def menu():
    titulo("CADASTRO DE PESSOAS")

    lista = ["[1] - Registrar novo cadastro.", "[2] - Buscar Cadastrados pelo id.", "[3] - Buscar Cadastrados pelo Email.", "[4] - Deletar Cadastrados pelo id.", "[5] - Deletar Cadastrados pelo Email.", "[6] - Atualizar cadastro.", "[7] - Sair"]

    for items in lista:
        print(items)
        print(linha())


def menu_atualizar():
    print(linha())
    print('''
1 - Nome
2 - Idade
3 - Email
4 - Telefone                              
          ''')
        
        