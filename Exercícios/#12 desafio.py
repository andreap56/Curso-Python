#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

Preço = float(input("Qual é o preço do produto? R$"))

Desconto = 0.05*Preço

Final = Preço - Desconto

print ("O seu produto de R${:.2f} com o desconto de 5%, terá o seu valor final de R${:.2f}.".format(Preço,Final))

#OU

preço = float(input("Qual é o preço do produto? R$"))
novo = preço - (preço * 5 / 100)

print ("O produto que custava R${}, na promoção com o desconto de 5% vai custar R${:.2f}".format(preço, novo))