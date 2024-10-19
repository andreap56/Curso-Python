# Mensagem de boas-vindas ao usuário
print("Bem vindos a lista de contatos do André Pereira")
print("-"*50)  # Linha de separação
print("-"*18 + "MENU PRINCIPAL" + "-"*18)  # Título do menu principal

lista_contatos = []  # Lista para armazenar os contatos
id_global = 4970340  # ID inicial global para os contatos

# Função para cadastrar um novo contato
def cadastrar_contato(id):
    print("-"*50)  # Linha de separação
    print("-"*8 + "MENU CADASTRAR" + "-"*8)  # Título do menu de cadastro

    # Solicita as informações do contato
    idContato = input("Id do contato: ")
    nome = input("Por favor entre com o nome do contato: ")
    atividade = input("Por favor entre com a atividade do contato: ")
    telefone = input("Por favor entre com o telefone do contato: ")

    # Cria um dicionário com os dados do contato
    contato = {
        "id": id,
        "nome": nome,
        "atividade": atividade,
        "telefone": telefone
    }
    lista_contatos.append(contato.copy())  # Adiciona o contato à lista
    print("Contato criado!")  # Confirmação de cadastro

# Função para consultar contatos
def consultar_contatos():
    print("-"*50)  # Linha de separação
    print("-"*8 + "MENU CONSULTAR CONTATOS" + "-"*8)  # Título do menu de consulta
    while True:
        # Solicita a opção de consulta ao usuário
        opcao = int(input("Escolha a opção que deseja:\n1 - Consultar Todos os Contatos\n2 - Consultar Contato por ID\n3 - Consultar Contato(s) por atividade\n4 - Retornar \n>>"))

        if opcao == 1:  # Consultar todos os contatos
            if not lista_contatos:
                print("Nenhum contato cadastrado.")  # Mensagem se não houver contatos
            else:
                for contato in lista_contatos:  # Itera pela lista de contatos
                    # Exibe as informações do contato
                    print("ID: {}".format(contato["id"]))
                    print("Nome: {}".format(contato["nome"]))
                    print("Atividade: {}".format(contato["atividade"]))
                    print("Telefone: {}".format(contato["telefone"]))
                    print()
                    print("-"*18)  # Linha de separação entre contatos
        elif opcao == 2:  # Consultar contato por ID
            id_consulta = int(input("Informe o ID do contato: "))
            for contato in lista_contatos:
                if contato["id"] == id_consulta:  # Verifica se o ID corresponde a um contato
                    # Exibe as informações do contato
                    print("ID: {}".format(contato["id"]))
                    print("Nome: {}".format(contato["nome"]))
                    print("Atividade: {}".format(contato["atividade"]))
                    print("Telefone: {}".format(contato["telefone"]))
                    print()
                    print("-"*18)  # Linha de separação
                    break
            else:
                print("Contato não encontrado.")  # Mensagem se o contato não for encontrado
        elif opcao == 3:  # Consultar contato por atividade
            atividade_consulta = input("Informe a atividade: ")
            for contato in lista_contatos:
                if contato["atividade"].lower() == atividade_consulta.lower():  # Verifica se a atividade corresponde
                    # Exibe as informações do contato
                    print("ID: {}".format(contato["id"]))
                    print("Nome: {}".format(contato["nome"]))
                    print("Atividade: {}".format(contato["atividade"]))
                    print("Telefone: {}".format(contato["telefone"]))
                    print()
                    print("-"*18)  # Linha de separação
        elif opcao == 4:  # Retorna ao menu principal
            return
        else:
            print("Opção inválida")  # Mensagem se a opção for inválida

# Função para remover um contato
def remover_contato():
    print("-"*50)  # Linha de separação
    print("-"*18 + "MENU REMOVER CONTATOS" + "-"*18)  # Título do menu de remoção
    while True:
        id_remover = int(input("Digite o ID do contato a ser removido: "))  # Solicita o ID do contato a ser removido
        for contato in lista_contatos:
            if contato["id"] == id_remover:  # Verifica se o ID corresponde a um contato
                lista_contatos.remove(contato)  # Remove o contato da lista
                print("Contato removido com sucesso!")  # Confirmação de remoção
                return
        print("ID inválido")  # Mensagem se o ID for inválido

# Loop principal do programa
while True:
    # Solicita a opção desejada ao usuário
    opcao_menu = int(input("Escolha a opção desejada:\n1 - Cadastrar contato\n2 - Consultar Contato\n3 - Remover contato\n4 - Sair\n>> "))

    if opcao_menu == 1:  # Cadastrar contato
        id_global += 1  # Incrementa o ID global
        cadastrar_contato(id_global)  # Chama a função para cadastrar o contato
    elif opcao_menu == 2:  # Consultar contato
        consultar_contatos()  # Chama a função para consultar contatos
    elif opcao_menu == 3:  # Remover contato
        remover_contato()  # Chama a função para remover contato
    elif opcao_menu == 4:  # Sair do programa
        print("Programa encerrado.")  # Mensagem de encerramento
        break  # Sai do loop
    else:
        print("Opção inválida")  # Mensagem se a opção for inválida
