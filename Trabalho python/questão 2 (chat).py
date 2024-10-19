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
