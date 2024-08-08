#Faça um programa que leia a largura e a altura em metros. Calcule a sua área e a quantidade de tinta necessária para pintá-la. Sabendo que cada litro de tinta pinta um área de 2m quadrados

l = float(input("Qual a largura de sua parede em metros? "))
a = float(input("Qual a altura de sua parede em metros? "))
ar = l*a
l = ar/2

print ("O quanto de tinta que você gastará será de {} litros".format(l))
