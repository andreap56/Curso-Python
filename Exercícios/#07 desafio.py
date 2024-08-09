#Desenvolva um programa que leia as duas notas de um aluno. Carlcule e mostre sua média

n1 = float(input("Qual foi a primeira nota do aluno? "))
n2 = float(input("Qual foi a segunda nota do aluno? "))

m = (n1+n2)/2

print ("A média do aluno será: {:.1f}".format(m))