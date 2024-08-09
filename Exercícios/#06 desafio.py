#CRIE UM ALGORITMO QUE LEIA UM NÚMERO E MOSTRE O SEU DOBRO, TRIPLO E RAIZ QUADRADA

n = int(input("Escolha um número: "))
d = n * 2
t = n * 3
rq = n ** (1/2)

print ("O dobro de {} será {}\nO seu triplo será {}\nA sua raiz quadrada será {:.2f}".format(n,d,t,rq))
#Lembre-se que {:.2f} seria para abreviar o número decimal em apenas duas casas após a vírgula

#OU

n = int(input("Escolha um número: "))

print ("O dobro de {} será {}\nO seu triplo será {}\nAsua raíz quadrada será {:.2f}".format(n, (n*2), (n*3), pow(n, (1/2))))