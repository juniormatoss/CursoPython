import random
import os

numero_aleatorio = random.randint(0, 100)
repetir = True
entradas = []

while repetir:
    entrada = int(input("Digite um número de 0 a 100: "))
    
    if entrada != numero_aleatorio:
        if entrada > numero_aleatorio:
            print("O número é menor")
            entradas.append(entrada)
        else:
            print("O número é maior")
            entradas.append(entrada)
    else:
        entradas.append(entrada)
        os.system('clear'),
        print("Você digitou os números:", ", ".join(map(str, entradas)))
        print("O número certo é:", numero_aleatorio)
    
        repetir = False
