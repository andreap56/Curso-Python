#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado

km = float(input("Quantos KM o carro alugado percorreu? "))
d = int(input("Quantos dias o carro foi alugado? "))

km2 = 60 * km
d2 = 0.15 * d
p = km2 + d2

print ("O preço a pagar do carro alugado corresponde {:.2f}.".format(p))
