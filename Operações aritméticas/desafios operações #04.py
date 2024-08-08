#Escreva um programa que leia um valor em metros e o exiba convertido em cenimetros e milimetros

M = float(input("Escreva um valor em metros: "))
Cen = M * 100
Mil = M * 1000

print ("A conversão do valor para centímetros será: {}\nA conversão do valor para milímetros será {}".format(Cen,Mil))