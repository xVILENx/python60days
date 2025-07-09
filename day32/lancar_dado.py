import random

def lancar_dado():
    """ 
    Simular o lancamento de um dado de 1 a 6
    
    Return: 
        int: um numero aleatorio de 1 a 6
    """
    
    return random.randint(1, 6)

if __name__ == "__main__":
    print(f"O resulatdo do dado foi: {lancar_dado()}")
    
    