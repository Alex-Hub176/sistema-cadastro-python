import pacote

pessoa = {}
dados = []



while True:

    pacote.Interface.menu()
    escolha = str(input("Escolha: ")).strip()
    pacote.Interface.linha()
    

    if escolha == "1":
            nome = str(input("Nome: "))
            idade = pacote.Validacao.idade()
            email = str(input("Email: "))
            telefone = str(input("Número de Telefone: "))

            pacote.inserir.adicionar(nome,idade,email,telefone)
        

    elif escolha == "2":
        id = int(input("Id: "))
        pacote.consulta.buscar(id,1)

    elif escolha == "3":
        email = str(input("Email: ")).strip()
        pacote.consulta.buscar(email,2)

    elif escolha == "4":
        id = int(input("Id: "))  
        pacote.deletar.delete(id,1)

    elif escolha == "5":
        email = str(input("Email: ")).strip()
        pacote.deletar.delete(email,2)
    
    elif escolha == "6":
         break
    

    

    
