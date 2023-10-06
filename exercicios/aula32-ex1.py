numero = int(input("Digite um numero inteiro: 22"))

if type(numero) == int:
    if numero%2==0:
        print("É par")
    else:
        print("É impar")

else:
    print ("Você não digitou um numero ineiro")