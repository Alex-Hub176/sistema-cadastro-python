import pacote

print('--'*10)
print("   CADASTRO DE PESSOAS    ")
print('--'*10)

pessoa = {}
dados = []

while True:
    print("""
        Oque você quer fazer?
        [1] Registrar novo Cadastro.
        [2] Buscar Cadastrados pelo Nome.
        [3] Buscar Cadastrados pelo Teléfone.
        [4] Deletar Algum Cadastrado.
        [5] Sair
        """)
    escolha = str(input("Escolha: ")).strip()

    while escolha not in ["1","2","3","4","5"]:
        print("ERRO! Escolha uma dessas opções")
        print("""
        [1] Registrar novo Cadastro.
        [2] Buscar Cadastrados pelo Nome.
        [3] Buscar Cadastrados pelo Teléfone.
        [4] Deletar Algum Cadastrado.
        [5] Sair
         """)
        escolha = str(input("Escolha: ")).strip()

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
    
    

    

    
