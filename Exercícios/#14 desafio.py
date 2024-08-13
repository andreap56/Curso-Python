#Escreva um programa que converta uma temperatura digitada em °C e coverta para °F

C = float(input("Escreva a temperatura em °C: "))
F = (C * 1.8) + 32

print ("A temperatura de {}°C corresponde {}°F".format(C,F))