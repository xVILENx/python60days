def dividir(numerador, denominador):
    try:
        resultado = numerador / denominador
        print(f"O resultado da divisao é {resultado}.")
    except ZeroDivisionError:
        print("A divisão por 0 não pode ocorrer.")
    except TypeError:
        print("O código não pode aceitar strings, apenas numeros.")
    print("Função rodou.")
    
        
if __name__ == "__man__":
    dividir(5,2)
    