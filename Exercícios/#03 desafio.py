#Peça para o usuário digitar dois valores para no final mostrar a soma entre eles

valor1 = int(input("Digite um valor:"))
valor2 = int(input("Digite outro valor:"))
print (f"A soma entre os valores {valor1} e {valor2} é igual a {valor1 + valor2}")

#ou

n1 = int(input ("Digite um valor:"))
n2 = int(input ("Digite outro valor:"))
s = n1 + n2
print ("A soma entre os valores {} e {} é igual a {}".format (n1,n2,s))