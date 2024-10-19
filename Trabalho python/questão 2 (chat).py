print("     Bem-vindo à pizzaria do André Pereira")
print("-" * 50)
print("                 Cardápio")
print("-" * 50)
print(" Tamanho | Pizza Salgada (PS) | Pizza Doce (PD)")
print("-" * 50)
print ("          P | R$ 30,00 | R$ 34,00")
print ("          M | R$ 45,00 | R$ 48,00")
print ("          G | R$ 60,00 | R$ 66,00")
print("-" * 50)

total = 0

while True:

    sabor = input("Entre com o sabor desejado (PS/PD): ")
    if sabor not in ["PS", "PD"]:
        print('Tente novamente. Sabor inválido!')
        continue

    tamanho = input("Qual o tamanho que você deseja (P, M ou G)?")
    if tamanho not in ["P", "M", "G"]:
        print ("Tamanho inválido!")
        continue 

    if sabor == "PS":
        if tamanho == "P":
            preco = 30.00
        elif tamanho == "M":
            preco = 45.00
        elif tamanho == "G":
            preco = 60.00

    elif sabor == "PD":
        if tamanho == "P":
            preco = 34.00
        elif tamanho == "M":
            preco = 48.00
        elif tamanho == "G":
            preco = 66.00

    if sabor == "PS":
        print ("Você escolheu uma pizza salgada no tamanho {}: R$ {:.2f}".format(tamanho, preco))
    else:
        print ("Você escolheu uma pizza doce no tamanho {}: R$ {:.2f}".format(tamanho, preco))

    total += preco

    MaisUmPedido = input("Deseja mais alguma coisa? (S/N): ")
    if MaisUmPedido == "N":
        break

print ("O valor total a ser pago será de: R$ {:.2f}".format(total))
# Mensagem de boas-vindas ao usuário
print("     Bem-vindo à pizzaria do André Pereira")
print("-" * 50)  # Linha de separação
print("                 Cardápio")  # Título do cardápio
print("-" * 50)  # Linha de separação
print(" Tamanho | Pizza Salgada (PS) | Pizza Doce (PD)")  # Cabeçalho do cardápio
print("-" * 50)  # Linha de separação
# Exibição dos preços das pizzas
print("          P | R$ 30,00 | R$ 34,00")
print("          M | R$ 45,00 | R$ 48,00")
print("          G | R$ 60,00 | R$ 66,00")
print("-" * 50)  # Linha de separação

total = 0  # Inicializa o total a ser pago

# Loop para processar os pedidos
while True:
    # Solicita ao usuário o sabor da pizza
    sabor = input("Entre com o sabor desejado (PS/PD): ")
    if sabor not in ["PS", "PD"]:  # Verifica se o sabor é válido
        print('Tente novamente. Sabor inválido!')
        continue  # Volta ao início do loop se o sabor for inválido

    # Solicita ao usuário o tamanho da pizza
    tamanho = input("Qual o tamanho que você deseja (P, M ou G)? ")
    if tamanho not in ["P", "M", "G"]:  # Verifica se o tamanho é válido
        print("Tamanho inválido!")
        continue  # Volta ao início do loop se o tamanho for inválido

    # Determina o preço com base no sabor e no tamanho
    if sabor == "PS":
        if tamanho == "P":
            preco = 30.00
        elif tamanho == "M":
            preco = 45.00
        elif tamanho == "G":
            preco = 60.00
    elif sabor == "PD":
        if tamanho == "P":
            preco = 34.00
        elif tamanho == "M":
            preco = 48.00
        elif tamanho == "G":
            preco = 66.00

    # Exibe a escolha do usuário e o preço
    if sabor == "PS":
        print("Você escolheu uma pizza salgada no tamanho {}: R$ {:.2f}".format(tamanho, preco))
    else:
        print("Você escolheu uma pizza doce no tamanho {}: R$ {:.2f}".format(tamanho, preco))

    total += preco  # Atualiza o total com o preço da pizza escolhida

    # Pergunta se o usuário deseja fazer mais um pedido
    MaisUmPedido = input("Deseja mais alguma coisa? (S/N): ")
    if MaisUmPedido == "N":  # Se o usuário não quiser mais nada, sai do loop
        break

# Exibe o valor total a ser pago
print("O valor total a ser pago será de: R$ {:.2f}".format(total))
