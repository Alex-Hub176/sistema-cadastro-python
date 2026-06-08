import json
import pacote

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
                print(pacote.Interface.linha())
                print(f"Nome: {pessoa["nome"]}\n Idade: {pessoa["idade"]} \n Número: {pessoa["numero"]}\n DDD: {pessoa["ddd"]} \n UF: {buscar_uf(pessoa["ddd"])} \n")
                print(pacote.Interface.linha())
        elif escolhas == "3":
            if pessoa["numero"] == numero:
                print(pacote.Interface.linha())
                print(f"Nome: {pessoa["nome"]}\n Idade: {pessoa["idade"]} \n Número: {pessoa["numero"]}\n DDD: {pessoa["ddd"]} \n UF: {buscar_uf(pessoa["ddd"])} \n")
                print(pacote.Interface.linha())
    return None