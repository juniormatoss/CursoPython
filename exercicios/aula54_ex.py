import os

lista = []

while True:
    print ("selecione uma opção")
    opcao = input("[i] inserir [a]apagar [l]listar [s]sair: ")

    if opcao == "i":
        os.system("clear")
        valor = input("Digite o nome do produto: ")
        lista.append(valor)

    elif opcao == "a":
        indice_str = input("Digite o indice para apagar  : ")


        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print("Digite numeros inteiros: ")
        except IndexError:
            print("indice não existe na lista:")
        except Exception:
            print("Erro desconhecido: ")

    elif opcao == "l":
        os.system("clear")

        if len(lista) == 0:
            print("Nada para listar")

        for i, valor in enumerate(lista):
            print(i, valor)
            
    elif opcao == "s":
        os.system("clear")
        print("Até Mais")
        break
    
    else:
        os.system("clear")
        print("por favor escola [i], [a] ou [l].")
        
        
