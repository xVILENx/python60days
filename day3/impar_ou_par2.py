entrada = input("Coloque o numero desejado:")

try:  #tente rodar
    numero = int(entrada)
    if numero % 2 == 0:
        print("Numero par")
    else:
        print("Numero impar")

except ValueError:
    print("Essa entrada não é um numero inteiro")