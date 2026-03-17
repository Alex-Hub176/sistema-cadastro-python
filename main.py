import pacote

pessoa = {}
dados = []



while True:

    pacote.Interface.menu()
    escolha = str(input("Escolha: ")).strip()
    pacote.Interface.linha()
    

    if escolha == "1":
            pessoa["nome"] = str(input("Nome: "))
            pessoa["idade"] = pacote.Validacao.idade()
            pessoa["numero"] = str(input("Número de Telefone: "))
            pessoa["ddd"] = pessoa["numero"][0:2]
            pessoa["uf"] = pacote.Buscar.buscar_uf(pessoa["ddd"])

            pacote.Salvar_Deletar.salvar_dados(pessoa)
        

    elif escolha == "2":
        nome = str(input("Nome: ")).strip()
        pacote.Buscar.buscar_pessoa("2",nome=nome)

    elif escolha == "3":
        telefone = str(input("Telefone: ")).strip()
        pacote.Buscar.buscar_pessoa("3",numero=telefone)

    elif escolha == "4":
        deletar = str(input("Digite o número do Telefone de quem você quer Deletar: "))  
        pacote.Salvar_Deletar.deletar_pessoa(deletar)

    elif escolha == "5":
        break
    
    

    

    
