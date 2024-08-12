#Escreva um valor em real para depois escrever o quanto de dolares é capaz de comprar

r = float(input("Quanto dinheiro você tem na carteira? R$"))

d = r/5.70

print ("Com R${:.2f} reais você poderá comprar US${:.2f}!".format(r,d))