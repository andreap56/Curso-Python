#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

sal = float(input("Escreva o seu salário: R$"))
por = sal * 0.15
aum = por + sal 

print ("O salário de R${:.2f} com o aumento de 15% será de R${:.2f}".format(sal,aum))