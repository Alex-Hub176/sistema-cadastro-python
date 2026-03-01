import json

def salvar_dados(dados):
    with open("pessoas.json", "r") as f:
        pessoas = json.load(f)

    pessoas.append(dados)
    
    with open("pessoas.json", "w") as f:
        json.dump(pessoas, f, indent=4)


def deletar_pessoa(numero):
    with open("pessoas.json", "r") as f:
        pessoas = json.load(f)

    while not any(p["numero"] == numero for p in pessoas):
        print("Número não encontrado. \n Tente novamente!")
        numero = input("Digite um número válido: ").strip()
        continuar = str(input("Que continuar? [S/N]: ")).strip().upper()[0]
        if continuar == "N":
            break

        
    for pessoa in pessoas:
        if pessoa["numero"] == numero:
            print(f"Será apagada essa pessoa {pessoa}")

        while True:
            resposta = str(input("Tem certeza? [S/N]: ")).strip().upper()[0]
            if resposta in ("S", "N"):
                break
            print("Digite apenas S ou N.")

        if resposta == "S":
            pessoas.remove(pessoa)
            print("APAGADO")
        break

    with open("pessoas.json", "w") as f:
            json.dump(pessoas, f, indent=4)

    
