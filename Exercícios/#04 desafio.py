#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele

a = input ("Digite Algo: ")

print ("O tipo primitivo desse valor é", type(a))
#print ("Possui espaços?", "sim" if a.isspace () else "não") CONDICIONAIS VOU APRENDER MAIS A FRENTE
print ("É um número?", a.isnumeric ())
print ("É um identificador?", a.isidentifier ())
print ("É printável?", a.isprintable())
