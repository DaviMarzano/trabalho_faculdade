def escolhaModelo():
    # Função de escolha de modelo do cliente, aonde retorno valor com base no modelo escolhido
    while True:  
        print("Entre com o modelo desejado")
        print("MCS - Manga Curta Simpels")
        print("MLS - Manga Longa Simples")
        print("MCE - Manga Curta com Estampa")
        print("MLE - Manga Longa com Estampa")
        modelo = input(">>>")
        
        if modelo in ["MCS", "MLS", "MCE", "MLE"]:

            if modelo == "MCS":
                valor_camiseta = 1.80
                return valor_camiseta
            elif modelo == "MLS":
                valor_camiseta = 2.10
                return valor_camiseta
            elif modelo == "MCE":
                valor_camiseta = 2.90
                return valor_camiseta
            elif modelo == "MLE":
                valor_camiseta = 3.20
                return valor_camiseta        

        else:
            print("Escolha inválida, entre com o modelo novamente.\n ")


def numCamisetas():
    # Função para calculo do número de camisetas que retorno o valor com desconto aplicado
    while True:

        try:
            quantidade_escolhida = int(input("Entre com o número de camisetas: "))
            if quantidade_escolhida > 20000:
                print("Não aceitamos tantas camisetas de uma vez.")
                raise ValueError("Por favor, entre com o número de camisetas novamente.")    

            elif quantidade_escolhida < 20000:

                if quantidade_escolhida >= 20 and quantidade_escolhida < 200:
                    desconto_valor = (quantidade_escolhida * 5) / 100
                    return quantidade_escolhida - desconto_valor
                
                elif quantidade_escolhida >= 200 and quantidade_escolhida < 2000:
                    desconto_valor = (quantidade_escolhida * 7) / 100
                    return quantidade_escolhida - desconto_valor 
                
                elif quantidade_escolhida >= 2000 and quantidade_escolhida <= 20000:
                    desconto_valor = (quantidade_escolhida * 12) / 100
                    return quantidade_escolhida - desconto_valor 
            
        except ValueError as e:
            print(e) # Mostra a mensagem passada para o ValueError

        except Exception as e:
            print("Não foi possivel realizar a operação, tente novamente ")
            
def frete():
    # Função para calculo de frete da compra
    while True:
        print("Escolha o tipo de frete:")
        print("1 - Frete por transportadora - R$100.00")
        print("2 - Frete por Sedex - R$200.00 ")
        print("0 - Retirar pedido na fábrica - R$0.00")
        frete_escolhido = input(">>>")

        if frete_escolhido in ["1", "2", "0"]:

            if frete_escolhido == "1":                
                return 100.00
            
            elif frete_escolhido == "2":
                return 200.00
                
            else:               
                return 0            
        

# Programa principal

print("Bem vindo a Fábrica de Camisetas do Davi Marzano\n")

modelo_escolhido = escolhaModelo()
numero_camisetas = numCamisetas()
print()
frete_cliente = frete()

total = numero_camisetas * modelo_escolhido + frete_cliente

# Saída final do programa
print(f"Total: R${total:.2f} (Modelo: {modelo_escolhido:.2f} * Quantidade(com desconto): {numero_camisetas:.0f} + frete: {frete_cliente:.2f}: )")

