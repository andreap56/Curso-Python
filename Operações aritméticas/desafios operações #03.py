#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a média
Aluno = input("Qual o nome do Aluno? ")
nota1 = int(input("Qual foi a nota da primeira avaliação de {}? ".format(Aluno) ))
nota2 = int(input("Qual foi a nota da segunda avaliação de aluno {}? ".format(Aluno)))

m = (nota1+nota2)/2 #importante colocar os parenteses primeiro

print ("A média de {} será: {}" .format(Aluno,m))