#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

p = float(input("Qual o preço do produto? "))
d = 0.05*p
e = p-d

print ("O preço do produto com 5% de desconto será de {}!".format(e))