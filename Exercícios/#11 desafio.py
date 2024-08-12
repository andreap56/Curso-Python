#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m²

largura = float(input("Qual a largura de sua parede? "))
altura = float(input("Qual a altura de sua parede? "))

área = largura * altura 
tinta = área / 2

print ("A sua parede possui uma largura de {}m e uma altura de {}m.\nPortanto, a área será de {}m² e a quantidade de tinta necessária será de {}l".format(largura,altura,área,tinta))