def mostrar_menu():
    print("--------- Bem-vindo a Loja de Marmitas do Davi Marzano ----------")
    print(27 * "-", "Cardápio", 28 * "-")
    print("---|  Tamanho  |  Bife Acebolado(BA) |  Filé de Frango(FF)   |---")
    print("---|     P     |       R$ 16.00      |       R$ 15.00        |---")
    print("---|     M     |       R$ 18.00      |       R$ 17.00        |---")
    print("---|     G     |       R$ 22.00      |       R$ 21.00        |---")

total_pedido = 0.0

mostrar_menu()

while True:
    sabor_usuario = input("Entre com o sabor desejado (BA/FF): ").upper()

    if sabor_usuario == "BA": # Caso seja bife acebolado
        tamanho_escolhido = input("Entre com o tamanho desejado (P/M/G): ").upper()

        if tamanho_escolhido not in ["P", "M", "G"]: # Verificação de tamanhos
            print("Tamanho inválido. Tente novamente ")
                
        elif tamanho_escolhido == "P":
            valor_bife = 16.00
            print(f"Você pediu um Bife Acebolado no tamanho {tamanho_escolhido}: R${valor_bife:.2f}")
            escolha_cliente = input("Deseja mais alguma coisa? (S/N) ")
            total_pedido += valor_bife
            if escolha_cliente == "S":
                continue
            else:
                print(f"Valor total a ser pago é de R${total_pedido:.2f}")
                break

        elif tamanho_escolhido == "M":
            valor_bife = 18.00
            print(f"Você pediu um Bife Acebolado no tamanho {tamanho_escolhido}: R${valor_bife:.2f}")
            escolha_cliente = input("Deseja mais alguma coisa? (S/N) ")
            total_pedido += valor_bife
            if escolha_cliente == "S":
                continue
            else:
                print(f"Valor total a ser pago é de R${total_pedido:.2f}")
                break

        elif tamanho_escolhido == "G":
            valor_bife = 16.00
            print(f"Você pediu um Bife Acebolado no tamanho {tamanho_escolhido}: R${valor_bife:.2f}")
            escolha_cliente = input("Deseja mais alguma coisa? (S/N) ")
            total_pedido += valor_bife
            if escolha_cliente == "S":
                continue
            else:
                print(f"Valor total a ser pago é de R${total_pedido}")
                break
 
    elif sabor_usuario == "FF": # Caso seja file de frango
        tamanho_escolhido = input("Entre com o tamanho desejado (P/M/G): ").upper()
        
        if tamanho_escolhido not in ["P", "M", "G"]:# Verificação de tamanhos
            print("Tamanho inválido. Tente novamente ")

        elif tamanho_escolhido == "P":
            valor_frango = 15.00
            print(f"Você pediu um Filé de Frango no tamanho {tamanho_escolhido}: R${valor_frango:.2f}")
            escolha_cliente = input("Deseja mais alguma coisa? (S/N) ")
            total_pedido += valor_frango
            if escolha_cliente == "S":
                continue
            else:
                print(f"Valor total a ser pago é de R${total_pedido}")
                break

        elif tamanho_escolhido == "M":
            valor_frango = 17.00
            print(f"Você pediu um Filé de Frango no tamanho {tamanho_escolhido}: R${valor_frango:.2f}")
            escolha_cliente = input("Deseja mais alguma coisa? (S/N) ")
            total_pedido += valor_frango
            if escolha_cliente == "S":
                continue
            else:
                print(f"Valor total a ser pago é de R${total_pedido}")
                break

        elif tamanho_escolhido == "G":
            valor_frango = 21.00
            print(f"Você pediu um Filé de Frango no tamanho {tamanho_escolhido}: R${valor_frango:.2f}")
            escolha_cliente = input("Deseja mais alguma coisa? (S/N) ")
            total_pedido += valor_frango
            if escolha_cliente == "S":
                continue
            else:
                print(f"Valor total a ser pago é de R${total_pedido:.2f}")
                break

    elif sabor_usuario not in ["BA", "FF"]:
        print("Sabor inválido. Tente novamente ")
        


    
    
