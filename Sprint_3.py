clientes = []
id = 0

print("\n---Bem vindo ao cadastro de clientes Salesforce---")

while True: 

    opcao = int(input("\nMENU:\n1 - Incluir\n2 - Exibir\n3 - Editar\n4 - Excluir\n5 - Sair\nR:"))
    
    if(opcao == 1):
        nome = input("Digite o nome: ")
        idade = input("Digite a idade: ")
        email = input("Digite o email: ")

        opcaoDef = input("\nPossui alguma deficiencia? (S/N)\nR:").upper()
        
        if(opcaoDef=="S"):
            deficiencia = int(input("\n1 - Daltonismo\n2 - Baixa visão"))
            
            if(deficiencia == 1):
                daltonismo = int(input("\nSelecione seu tipo de Daltonismo:\n1 - Deuteranopia\n2 - Protanopia\n3 - Tritanopia"))

                if(daltonismo == 1):
                    print("\nPredefinições do site alteradas para Deuteranopia")
                    deficiencia = "Deuteranopia"
                    
                elif(daltonismo == 2):
                    print("\nPredefinições do site alteradas para Protanopia")
                    deficiencia = "Protanopia"           

                else:
                    print("\nPredefinições do site alteradas para Tritanopia")  
                    deficiencia = "Tritanopia" 

            else:
                print("\nLeitor de tela ativado")    
                deficiencia = "Baixa visão"      
    
        else:
            deficiencia = "Não possui deficiência"

        id+=1

        dados = {"id":id, "nome":nome, "idade":idade, "email":email, "deficiencia":deficiencia}
        clientes.append(dados)
    
        input("\n---Aperte 'ENTER' para voltar para o Menu---")  

    elif(opcao == 2):
        opcaoCli = int(input("\n1 - Exibir todos os clientes\n2 - Exibir cliente específico\nR: "))

        if(opcaoCli == 1):
            for c in clientes:
                print(f"\nID: {c['id']}\nNome: {c['nome']}\nIdade: {c['idade']}\nE-mail: {c['email']}\nDeficiência: {c['deficiencia']}")

        else:
            def busca_por_nome(busca, clientes):
                for c in clientes:
                    if c["nome"] == busca:
                        return c
                return None

            busca = input("Digite o nome do cliente que deseja exibir: ")
            pessoa_encontrada = busca_por_nome(busca, clientes)

            if pessoa_encontrada:
                print(f"\nID: {pessoa_encontrada['id']}\nNome: {pessoa_encontrada['nome']}\nIdade: {pessoa_encontrada['idade']}\nE-mail: {pessoa_encontrada['email']}\nDeficiência: {pessoa_encontrada['deficiencia']}")
            
            else:
                print("\nCliente não encontrado")

        input("\n---Aperte 'ENTER' para voltar para o Menu---")          
    
    elif(opcao==3):
        for c in clientes:
            print(f"\nID: {c['id']}\nNome: {c['nome']}\nIdade: {c['idade']}\nE-mail: {c['email']}\nDeficiência: {c['deficiencia']}")

        escolha = int(input("\nDigite o ID do cliente que deseja atualizar: ")) - 1

        if 0 <= escolha < len(clientes):
            novo_nome = input("\nDigite o novo nome: ")
            nova_idade = int(input("Digite a nova idade: "))
            novo_email = input("Digite o novo email: ")
            clientes[escolha]['nome'] = novo_nome
            clientes[escolha]['idade'] = nova_idade
            clientes[escolha]['email'] = novo_email
                
            nova_opcao = input("O usuário possui deficiência?\n(S) para 'SIM'\n(N) para 'NÃO'\nR:").upper()
           
            if(nova_opcao == 'S'):
                opcao_nova_def = int(input("Escolha a nova deficiência:\n1 - Daltonismo\n2 - Baixa visão"))
                    
                if(opcao_nova_def == 1):
                    opcao_nova_daltonismo = int(input("Digite a nova opção de daltonismo:\n1 - Deuteranopia\n2 - Protanopia\n3 - Tritanopia"))

                    if(opcao_nova_daltonismo==1):
                            clientes[escolha]['deficiencia'] = "Deuteranopia"

                    elif(opcao_nova_daltonismo==2):
                            clientes[escolha]['deficiencia'] = "Protanopia"
                        
                    elif(opcao_nova_daltonismo==3):
                            clientes[escolha]['deficiencia'] = "Tritanopia"    

                    else: print("\nOpção inválida!")

                elif(opcao_nova_def == 2):
                    clientes[escolha]['deficiencia'] = "Baixa visão"

                else:
                    print("\nEscolha inválida.")

                print("\nCliente atualizado com sucesso!")

            elif(nova_opcao == 'N'):
                clientes[escolha]['deficiencia'] = "Não possui deficiência"

            else: print("Opção inválida!")    

        else:
            print("\nEscolha inválida.")
        
        input("\n---Aperte 'ENTER' para voltar para o Menu---")  

    elif(opcao == 4):
        def busca_por_id(opcaoId, clientes):
            for c in clientes:
                if c["id"] == opcaoId:
                    return c
            return None

        for c in clientes:
                print(f"\nID: {c['id']}\nNome: {c['nome']}\nIdade: {c['idade']}\nE-mail: {c['email']}\nDeficiência: {c['deficiencia']}")

        opcaoId = int(input("\nDigite o ID do cliente que deseja excluir: "))
        
        pessoa_encontrada = busca_por_id(opcaoId, clientes)

        if pessoa_encontrada:
            del clientes[opcaoId-1]
            print("\nCliente excluído com sucesso!") 
            
        else:
            print("\nCliente não encontrado")

        input("\n---Aperte 'ENTER' para voltar para o Menu---")         
       
    elif(opcao==5): break

    else: print("\nOpção inválida!")

    input("\n---Aperte 'ENTER' para voltar para o Menu---")

print("\nPrograma encerrado!")    