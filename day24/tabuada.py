def tabuada():
    """
    Essa funcao recebe um numero e retorna a tabuada desse numero
    """
    
    try:
        #solicitar o numero para o usuario
        
        numero = int(input("Digite o numero para gerar a tabuada: "))
        
        print(f"\n Tabuada de {numero}: ")
        #gera a tabuada de 1 a 10
        for i in range(1, 11):
            resultado = numero * i
            print(f"{numero} x {i} = {resultado}")
             
    except ValueError:
        print("ENtrada invalida. Digite um numero")

if __name__ == '__main__':
    tabuada()