#FAÇA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E MOSTRE NA TELA O SEU SUCESSOR E SEU ANTECESSOR

n = int(input("Escolha um número: "))
s = n+1
a = n-1

print ("O sucessor de {} será {} e o seu antecessor será {}".format(n,s,a))

#OU

n = int(input("Escolha um número: "))

print ("O sucessor de {} será {} e o seu antecessor será {}".format(n, (n+1), (n-1) ))