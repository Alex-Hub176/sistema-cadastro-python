import pacote


while True:

    pacote.Interface.menu()
    escolha = str(input("Escolha: ")).strip()
    pacote.Interface.linha()
    
    match escolha:

        case "1":
                nome = str(input("Nome: "))
                idade = pacote.Validacao.idade()
                email = str(input("Email: "))
                telefone = str(input("Número de Telefone: "))

                pacote.inserir.adicionar(nome,idade,email,telefone)
            

        case "2":
            while True:
                try:
                    id = int(input("Id: "))
                    pacote.consulta.buscar(id,1)
                    break
                except ValueError:
                    print("Digite números Inteiros")
                    


        case "3":
            email = str(input("Email: ")).strip()
            pacote.consulta.buscar(email,2)

        case "4":
            while True:
                try:
                    id = int(input("Id: "))  
                    pacote.deletar.delete(id,1)
                    break
                except ValueError:
                    print("Digite números Inteiros")

        case "5":
            email = str(input("Email: ")).strip()
            pacote.deletar.delete(email,2)
            
        case "6":
            pacote.Interface.menu_atualizar()
            opcao = input("Qual campo deseja atualizar? ")

            campos = {
                "1": "nome",
                "2": "idade",
                "3": "email",
                "4": "telefone"
            }

            campo = campos.get(opcao)
            
            if campo:
                id = int(input("Id: "))
                novo_valor = input("Novo valor: ").strip()
                pacote.atualizar.alterar(id, campo, novo_valor)


        case "7":
            break
        

    

    
