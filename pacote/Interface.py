
def linha(tam=44):
    return "-" * tam


def titulo(texto):
    print(linha())
    print(texto.center(40))
    print(linha())


def menu():
    titulo("CADASTRO DE PESSOAS")

    lista = ["[1] - Registrar novo cadastro.", "[2] - Buscar Cadastrados pelo Nome.", "[3] - Buscar Cadastrados pelo Teléfone.", "[4] - Deletar Cadastrados pelo Teléfone.", "[5] - Sair."]

    for items in lista:
        print(items)
        print(linha())
        
        