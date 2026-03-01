import json

def buscar_uf(ddd_usuario):
    with open("DDD_UF.json", "r") as f:
        dados_ddd = json.load(f)
    return dados_ddd.get(ddd_usuario, "Desconhecido")


def buscar_pessoa(escolhas, nome=None, numero=None):
    with open("pessoas.json", "r") as f:
        pessoas = json.load(f)

    for pessoa in pessoas:
        if escolhas == "2":
            if pessoa["nome"] == nome:
                print(pessoa)
        elif escolhas == "3":
            if pessoa["numero"] == numero:
                print(pessoa)

    return None