#Crie uma interação com o usuário perguntando o nome e tendo uma mensagem no final
nome = input("Digite seu nome:")
print (f"É um prazer te conhecer, {nome}!")
#ou
nome = input("Digite seu nome:")
print ("É um prazer te conhecer, {}!".format(nome))