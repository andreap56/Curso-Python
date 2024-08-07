#EFETUAR SOMA 
n1 = int(input("Selecione seu primeiro valor: ")) #Lembre-se sempre de colocar o int(input... para não dar erro
n2 = int(input("Selecione seu segundo valor: "))
s = (n1 + n2)
print ("A soma entre {} e {} será de {}".format (n1,n2,s))

#DESCOBRIR INFORMAÇÕES
a = input("Escreva algo aleatório")

print ("O tipo primitivo desse valor: ", type(a))
print ("Ele é um número? ", a.isalnum ())
print ("Ele é uma palavra?", a.isalpha ())
print ("Ele está capitalizado?", a.istitle ())