import os

lista = []



while True:
    print ("selecione uma opção")
    opcao = input("[i] inserir [a]apagar [l]listar: ")

    if opcao == "i":
        os.system("clear")
        valor = input("Digite o nome do produto")
        lista.append(valor)

    elif opcao == "a":
        indice_str = input("Digite o indice para apagar")


        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print("Digite numeros inteiros")
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')

    elif opcao == "l":
        os.system("clear")

        if len(lista) == 0:
            print("Nadfa para listar")

        for i, valor in enumerate(lista):
            print(i, valor)

    else:
        print("por favor escola i, a ou l.")