print("Bem-vindos a loja do Davi Marzano") #Saída inicial do programa

while True:
    try:
        valor_pedido = float(input("Entre com o valor do pedido: "))
        quantidade_parcelas = int(input("Entre com a quantidade de parcelas: "))
        
        if quantidade_parcelas < 4: 
            juros = 0
            valor_parcelas = valor_pedido / quantidade_parcelas
            print(f"O valor das parcelas é de: R${valor_parcelas:.2f}")
            print(f"O valor total parcelado é de: R${valor_pedido:.2f}")
        
        elif 4 <= quantidade_parcelas < 6: 
            juros = 0.04
            valor_parcelas = valor_pedido * (1 + juros) / quantidade_parcelas
            valor_total_parcelado = valor_parcelas * quantidade_parcelas
            print(f"O valor das parcelas é de: R${valor_parcelas:.2f}")
            print(f"O valor total parcelado é de: R${valor_total_parcelado:.2f}")
        
        elif 6 <= quantidade_parcelas < 9:
            juros = 0.08
            valor_parcelas = valor_pedido * (1 + juros) / quantidade_parcelas
            valor_total_parcelado = valor_parcelas * quantidade_parcelas
            print(f"O valor das parcelas é de: R${valor_parcelas:.2f}")
            print(f"O valor total parcelado é de: R${valor_total_parcelado:.2f}")
        
        elif 9 <= quantidade_parcelas < 13:
            juros = 0.16
            valor_parcelas = valor_pedido * (1 + juros) / quantidade_parcelas
            valor_total_parcelado = valor_parcelas * quantidade_parcelas
            print(f"O valor das parcelas é de: R${valor_parcelas:.2f}")
            print(f"O valor total parcelado é de: R${valor_total_parcelado:.2f}")
        
        elif quantidade_parcelas >= 13:
            juros = 0.32
            valor_parcelas = valor_pedido * (1 + juros) / quantidade_parcelas
            valor_total_parcelado = valor_parcelas * quantidade_parcelas
            print(f"O valor das parcelas é de: R${valor_parcelas:.2f}")
            print(f"O valor total parcelado é de: R${valor_total_parcelado:.2f}")
        break

    except ValueError: #Verificação se o usuario digitou apenas números
        print("Digite apenas números!")
        
    except :
        print("Não foi possível realizar a operação!")


