def fatorial(n):
    """
    Calcula o fatorial de um numero usando recursão.
    
    :param n: Número inteiro não negativo.
    :return: Fatorial de n.   
    """
    
    if n < 0:
        raise ValueError("O numero deve ser positivo")
    
    #entao essa condicional rertorna 1 se caso o numero da funcao for 0 ou 1
    if n == 0 or n == 1:
        return 1

    #recursividade    
    return n * fatorial(n - 1)
#print(fatorial(-1))

try:
    print(f"Fatorial igual a {fatorial(3)}")
except ValueError as e:
    print(e)