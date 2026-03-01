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


  

