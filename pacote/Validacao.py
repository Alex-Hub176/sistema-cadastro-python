def idade():
    while True:
        try:
            idade = int(input("Idade: "))
            if idade < 0 or idade >= 150:
                print("Idade inválida")
                continue
            return idade
        
        except ValueError:
            print("Digite números inteiros")


def pedir_email():
    while True:
        email = input("Email: ").strip()

        if "@" in email and "." in email:
            return email
        
        print("Email Inválido")


def pedir_id():
    while True:
        try:
            return int(input("Id: "))
        except ValueError:
            print("Digite um número inteiro")


def telefone():
    while True:
        numero = input("Telefone: ").strip()

        numero = (
            numero.replace("(","")
                .replace(")","")
                .replace("-","")
                .replace(" ","")

        )

        if not numero.isdigit():
            print("Telefone inválido.")
            continue

        if len(numero) not in (10, 11):
            print("Telefone inválido")
            continue

        return numero


  

