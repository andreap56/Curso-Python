print("Sistema desenvolvido por André Pereira") # Apresentação do Sistema

# Solicita ao usuário que informe o valor base do plano e converte para float
ValorBase = float(input("Informe qual seria o valor base do plano: R$")) # Pergunta sobre o valor base

# Solicita ao usuário que informe a idade do cliente e converte para inteiro
Idade = int(input("Qual a idade do cliente? ")) # Pergunta sobre a idade

# Ciclos de repetição com a exigência da porcentagem de acordo com cada faixa etária
if Idade >= 0 and Idade < 19: 
    porcentagem = 100 / 100 # 100% do valor base para clientes com menos de 19 anos

elif Idade >= 19 and Idade < 29:
    porcentagem = 150 / 100 # 150% do valor base para clientes de 19 a 28 anos

elif Idade >= 29 and Idade < 39:
    porcentagem = 225 / 100 # 225% do valor base para clientes de 29 a 38 anos

elif Idade >= 39 and Idade < 49:
    porcentagem = 240 / 100 # 240% do valor base para clientes de 39 a 48 anos

elif Idade >= 49 and Idade < 59:
    porcentagem = 350 / 100 # 350% do valor base para clientes de 49 a 58 anos

else:
    porcentagem = 600 / 100 # 600% do valor base para clientes com 59 anos ou mais

# Cálculo do valor mensal com base no valor base e na porcentagem definida
valorMensal = ValorBase * porcentagem # Cálculo do valor mensal

# Exibe o valor mensal formatado com duas casas decimais
print("O Valor Mensal do cliente é: R${:.2f}".format(valorMensal)) # Valor mensal
