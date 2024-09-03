#codigo = input("Digite o código do produto: ")
#nome = input("Digite o nome do produto: ")
#preço = float(input("Digte a quantidade em estoque: "))
#quantidade = int(input("Digite a quantidade em estoque: "))
#produtos[codigo] = {'nome': nome, 'preço': preço, 'quantidade': quantidade}
#print("Produto adicionado com sucesso!")
#print(produtos)
produtos = {}

while True:
    codigo = input("Digite o código do produto: ")
    nome = input("Digite o nome do produto: ")
    preço = float(input("Digte a quantidade em estoque: "))
    quantidade = int(input("Digite a quantidade em estoque: "))
    produtos[codigo] = {'nome': nome, 'preço': preço, 'quantidade': quantidade}
    print("Produto adicionado com sucesso!")
    print(produtos)
    
    continuar = input("Gostaria de fazer mais algum cadastro? [Sim/Não]")
    
    if continuar == 'não':
        print("Cadastro realizado")
        print(produtos)
        exit()
        
    elif continuar != 'sim':
       break
   
    else:
        print("Resposta invalida. Digite 'Sim' ou 'Não'.")