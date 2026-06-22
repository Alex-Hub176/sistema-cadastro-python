import pacote


while True:

    pacote.Interface.menu()
    escolha = str(input("Escolha: ")).strip()
    pacote.Interface.linha()
    
    match escolha:

        case "1":
                nome = str(input("Nome: "))
                idade = pacote.Validacao.idade()
                email = pacote.Validacao.pedir_email()
                telefone = pacote.Validacao.telefone()
            
                pacote.inserir.adicionar(nome,idade,email,telefone)
            

        case "2":
            id = pacote.Validacao.pedir_id()
            pacote.consulta.buscar(id,1)


        case "3":
            email = pacote.Validacao.pedir_email()
            pacote.consulta.buscar(email,2)

        case "4":
            id = pacote.Validacao.pedir_id()
            confirma = input("Tem certeza? (s/n): ").lower().strip()
            if confirma:
                pacote.deletar.delete(id,1)

        case "5":
            email = pacote.Validacao.pedir_email()
            confirmacao = input("Tem certeza? (s/n): ").lower().strip()
            if confirmacao:
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
                id = pacote.Validacao.pedir_id()
                novo_valor = input("Novo valor: ").strip()
                pacote.atualizar.alterar(id, campo, novo_valor)


        case "7":
            break
        

    

    
