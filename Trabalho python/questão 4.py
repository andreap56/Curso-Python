print("Bem vindos a lista de contatos do André Pereira")
print("-"*50)
print("-"*18 + "MENU PRINCIPAL" + "-"*18)

lista_contatos = []
id_global = 4970340

def cadastrar_contato(id):
    print("-"*50)
    print("-"*8 + "MENU CADASTRAR" + "-"*8)

    idContato = input("Id do contato: ")
    nome = input ("Por favor entre com o nome do contato: ")
    atividade = input ("Por favor entre com a atividade do contato: ")
    telefone = input("Por favor entre com o telefone do contato: ")

    contato = {
        "id": id,
        "nome": nome,
        "atividade": atividade,
        "telefone": telefone
     }
    lista_contatos.append(contato.copy())

    print ("Contato criado!")

    def consultar_contatos():
     print("-"*50)
     print("-"*8 + "MENU CONSULTAR CONTATOS" + "-"*8)
    while True:
        opcao = int(input("Escolha a opção que deseja:\n1 - Consultar Todos os Contatos\n2 - Consultar Contato por ID\n3 Consultar Contato(s) por atividade\n4 - Retornar \n>>"))


        if opcao == 1:
            if not lista_contatos:
                print("Nenhum contato cadastrado.")
            else:
                for contato in lista_contatos:
                    print("ID: {}".format(contato["id"]))
                    print("Nome: {}".format(contato["nome"]))
                    print("Atividade: {}".format(contato["atividade"]))
                    print("Telefone: {}".contato["telefone"])
                    print()
                    print("-"*18)
        elif opcao == 2:
            id_consulta = int(input("Infome o ID do contato:"))
            for contato in lista_contatos:
                if contato["id"] == id_consulta:
                    print("ID: {}".format(contato["id"]))
                    print("Nome: {}".format(contato["nome"]))
                    print("Atividade: {}".format(contato["atividade"]))
                    print("Telefone: {}".contato["telefone"])
                    print()
                    print("-"*18)
                    break
            else:
                print("Contato não encontrado.")
        elif opcao == 3:
            atividade_consulta = input("Informe a atividade: ") 
            for contatos in lista_contatos:
                if contato["atividade"].lower() == atividade_consulta.lower():
                    print("ID: {}".format(contato["id"]))
                    print("Nome: {}".format(contato["nome"]))
                    print("Atividade: {}".format(contato["atividade"]))
                    print("Telefone: {}".contato["telefone"])
                    print()
                    print("-"*18)
        elif opcao == 4:
            return
        else:
            print ("Opção inválida")

def remover_contato():
    print("-"*30)
    print("-"*18 + "MENU REMOVER CONTATOS" + "-"*18)
    while True:
        id_remover=int(input("Digite o ID do contato a ser removido: "))
        for contato in lista_contatos:
            if contato ["id"] == id_remover:
                lista_contatos.remover(contato)
                print("Contato removido com sucesso! ")
                return
        print("ID inválido")
    
    while True:
      opcao_menu = int(input("Escolha a opção desejada: (\n1 - Cadastrar contato\n2 - Consultar Contato\n3Remover contato\n4 - Sair \n>>)"))
      
      if opcao_menu == 1:
         id_global +=1
         cadastrar_contato(id_global)
      elif opcao_menu == 2:
         consultar_contatos()
      elif opcao_menu == 3:
         remover_contatos
      elif opcao_menu == 4:
         print ("Programa encerrado.")
         break
      else: 
        print ("Opção inválida")



