nome = input("Digite seu nome")

if (len(nome) <= 4):
    print("Pequeno")

elif(len(nome) >=5) and (len(nome) <= 6):
    print("seu nome é normal")

else:
    print("seu nome é grande")
