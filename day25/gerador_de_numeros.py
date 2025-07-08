import random

def gerar_numeros_aleatorios():
    """
    Gera numeros aleatorios imprimindo 10 nimeros entre 1 a 100
    """
    
    print("Bem vindo a ogerador de numeros aleatorios")
    
    numeros_aleatorios = []
    
    #gerar os numeros aleatorios
    for _ in range(10):
        numero = random.randint(1, 100) #gera num n aleatorio ente 1 a 100
        numeros_aleatorios.append(numero)
        
    print("\n Numeros aleatorios são: ")
    for i, numero in enumerate(numeros_aleatorios, start=1):
        print(f"Numero {i}: {numero}")
        
if __name__ == '__main__':
    gerar_numeros_aleatorios()