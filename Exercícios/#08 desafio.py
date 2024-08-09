#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

n = float(input("Selecione uma distância em metros: "))

cm = n * 100
mm = n * 1000

print ("A medida de {}m corresponde a {}cm e {}mm".format(n,cm,mm))

#Escreva um programa que leia um valor em metros convertendo em km, hm, dam, m, dm, cm, mm

m = float(input("Selecione uma distância em metros: "))

dm = n *10
cm = n * 100
mm = n * 1000
dam = n * 0.1
hm = n * 0.01
km = n * 0.001

print ("A medida de {}m corresponde a {}dm, {}cm, {}mm, {}dam,{}hm,{}km".format(m,dm,cm,mm,dam,hm,km))
