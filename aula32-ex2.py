hora = double(input("Digite a hopra"))

if (hora > 0) and (hora <= 11):
    print( "Bom dia")

elif (hora > 12) and (hora <= 17):
    print( "Boa tarde")

else:
    print("Boa noite")