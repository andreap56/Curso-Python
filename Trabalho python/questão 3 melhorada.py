# Mensagem de boas-vindas ao usuário
print("Bem vindo a Madeleira do Lenhador André Pereira!")

# Função para escolher o tipo de madeira e retornar seu preço
def escolha_tipo():
    while True:
        print("\nEntre com o Tipo de Madeira desejado:")
        print("PIN - Tora de Pinho")
        print("PER - Tora de Peroba")
        print("MOG - Tora de Mogno")
        print("IPE - Tora de Ipê")
        print("IMB - Tora de Imbuia")

        tipo = input(">>")  # Solicita ao usuário o tipo de madeira
        if tipo == "PIN":
            return 150.40  # Preço da tora de pinho
        elif tipo == "PER":
            return 170.20  # Preço da tora de peroba
        elif tipo == "MOG":
            return 190.90  # Preço da tora de mogno
        elif tipo == "IPE":
            return 210.10  # Preço da tora de ipê
        elif tipo == "IMB":
            return 220.70  # Preço da tora de imbuia
        else:
            print("Escolha errada, entre novamente com o modelo!")  # Mensagem de erro se a escolha for inválida

# Função para solicitar a quantidade de toras e retornar a quantidade e o desconto aplicável
def qtd_toras():
    while True:
        try:
            qtd = int(input("Entre com a quantidade de toras (m³): "))  # Solicita a quantidade de toras
            if qtd > 2000:
                print("Não aceitamos pedidos com essa quantidade de toras")  # Mensagem de erro se a quantidade for maior que 2000
            elif qtd < 100:
                return qtd, 0  # Sem desconto se a quantidade for menor que 100
            elif 100 <= qtd < 500:
                return qtd, 0.04  # 4% de desconto para quantidade entre 100 e 499
            elif 500 <= qtd < 1000:
                return qtd, 0.09  # 9% de desconto para quantidade entre 500 e 999
            elif 1000 <= qtd <= 2000:
                return qtd, 0.16  # 16% de desconto para quantidade entre 1000 e 2000
        except ValueError:
            print("Por favor, insira um valor numérico válido")  # Mensagem de erro se a entrada não for numérica

# Função para escolher o tipo de transporte e retornar seu custo
def transporte():
    while True:
        print("\nEscolha o tipo de transporte: ")
        print("1 - Transporte Rodoviário - R$1000.00")
        print("2 - Transporte Ferroviário - R$2000.00")
        print("3 - Transporte Hidroviário - R$2500.00")

        opcao = input(">>")  # Solicita ao usuário o tipo de transporte
        if opcao == "1":
            return 1000.00  # Custo do transporte rodoviário
        elif opcao == "2":
            return 2000.00  # Custo do transporte ferroviário
        elif opcao == "3":
            return 2500.00  # Custo do transporte hidroviário

# Bloco principal do programa
if __name__ == "__main__":
    valor_madeira = escolha_tipo()  # Chama a função para escolher o tipo de madeira

    qtd, desconto = qtd_toras()  # Chama a função para obter a quantidade de toras e o desconto

    valor_transporte = transporte()  # Chama a função para escolher o transporte

    # Cálculo do total considerando a quantidade, desconto e custo do transporte
    total = ((valor_madeira * qtd) * (1 - desconto)) + valor_transporte

    # Exibe o valor total a ser pago
    print("Total: R$ {:.2f}".format(total))
