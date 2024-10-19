print("Sistema desenvolvido por André Pereira") #Apresentação do Sistema

ValorBase = float(input("Informe qual seria o valor base do plano: R$")) #Pergunta sobre o valor base
Idade = int(input("Qual a idade do cliente? ")) #Pergunta sobre a idade

#Ciclos de repetição com a exigência da porcentagem de acordo com cada faixa etária
if Idade >=0 and Idade <19: 
    porcentagem = 100/100

elif Idade >=19 and Idade <29:
    porcentagem = 150/100

elif Idade >=29 and Idade <39:
    porcentagem = 225 / 100

elif Idade >=39 and Idade <49:
    porcentagem = 240 / 100

elif Idade >=49 and Idade <59:
    porcentagem = 350 / 100

else: porcentagem = 600 / 100

valorMensal = ValorBase * porcentagem #Cálculo do valor mensal
print ("O Valor Mensal do cliente é: R${:.2f}".format(valorMensal)) #Valor mensal

