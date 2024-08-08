#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário. Com 15% de aumento.

nome = input("Qual o nome de seu funcionário? ")
sal = float(input("Qual o salário de {}? ".format(nome)))
sal2 = 0.15*sal
sal3 = sal+sal2

print ("O salário de {} será: {} reais com o aumento de 15%!".format (nome,sal3))