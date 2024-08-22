def cadastrarFuncionario(id):
    # Função para cadastro de funcionarios
    print(35 * "-")
    print("-- Menu Cadastrar Funcionário --")
    print(f"Id do Funcionário: {id}")
    nome = input("Por favor entre com o nome do Funcionário: ")
    setor = input("Por favor entre com o setor do Funcionário: ")
    salario = float(input("Por favor entre com o salário do Funcionário: "))
    print(35 * "-")
    
    funcionarios = {
        "id": id,
        "nome": nome,
        "setor": setor,
        "salario": salario,
    }

    # Dados do dicionário inseridos na lista
    lista_funcionarios.append(funcionarios.copy())

def consultarFuncionarios():
    # Função para consulta de funcionários
    while True:
        print(35 * "-")
        print("-- Menu Consultar Funcionário --")
        print("1 - Consultar todos os Funcionários")
        print("2 - Consultar Funcionário por id")
        print("3 - Consultar Funcionário(s) por setor")
        print("4 - Retornar")
        escolha = input(">>>")

        if escolha in ["1", "2", "3", "4"]:

            if escolha == "1": #Consulta de todos os funcionários sem id
             for funcionario in lista_funcionarios:
                for chave, valor in funcionario.items():
                    print(f"{chave}: {valor}")
                    print()
                
            elif escolha == "2": #Consulta de funcionário por id
                id_digitado = int(input("Digite o id do funcionário: "))

                for funcionario in lista_funcionarios:

                    if funcionario["id"] == id_digitado:
                        
                        for chave, valor in funcionario.items():
                                print(f"{chave}: {valor}")
                        print()     
                        break
                    else:
                        print("Funcionário não encontrado.")         
            
            elif escolha == "3": # Consulta de funcionários por setor
                setor_digitado = input("Digite o setor do(s) funcionário(s): ")

                for funcionario in lista_funcionarios:

                    if funcionario["setor"] == setor_digitado:
                        print()
                        for chave, valor in funcionario.items():
                            print(f"{chave}: {valor}")
                        print()
                            
            elif escolha == "4":
                return

def removerFuncionario():
    #Função para remoção de funcionários
    print(35 * "-")
    print("----- Menu Remover Funcionário ----")
    id_remocao = int(input("Digite o id do funcionário a ser removido: "))
    
    for funcionario in lista_funcionarios:
        try:
            if funcionario["id"] == id_remocao:
                lista_funcionarios.remove(funcionario)
                print(f"Funcionário removido com sucesso!")
                print()
                break
            else:
                print("Funcionário não encontrado")

        except ValueError:
            print("Digite apenas números.")

# Programa principal

lista_funcionarios = []
id_global = 4991101

print("Bem vindo a Empresa do Davi Marzano")

while True:
    #Menu principal
    print(35 * "-")
    print("--------- Menu Principal ----------")
    print("Escolha a opção desejada:")
    print("1 - Cadastrar Funcionários")
    print("2 - Consultar Funcionário(s)")
    print("3 - Remover Funcionário")
    print("4 - Sair")
    escolha = input(">>>")

    if escolha in ["1", "2", "3", "4"]:
        if escolha == "1":
            cadastrarFuncionario(id_global)
            id_global = id_global + 1
        elif escolha == "2":
            consultarFuncionarios()
        elif escolha == "3":
            removerFuncionario()
        elif escolha == "4":
            break
    else:
        print("Opção inválida")



