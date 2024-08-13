# import bebida seria mais generalista
# from bebida importe escolho somente um
# import math inclue algumas funcionalidades matemáticas extras
# import math ceil faz um arredondamento para cima
# import math flor faz um arredondamento para baixo
# import math trunc vai tirar o número depois da vírgula
# import math pow trabalha com a potencia
#import sqrt vai trabalhar a raiz quadrada
#import factorial vai trabalhar com a fatorial de um número
#from math import sqrt só vai importar a raiz quadrada

import math
num = int(input("Digite um número: "))
raiz = math.sqrt(num)
print ("A raiz de {} é igual a {:.2f}".format(num, math.floor(raiz)))

from math import sqrt, floor
num = int(input("Digite um número: "))
raiz = sqrt(num)
print ("A raiz de {} é igual a {:.2f}".format(num, floor(raiz)))