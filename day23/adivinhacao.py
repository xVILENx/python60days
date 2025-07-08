import random

def jogar_adivinhacao():
    """
    
    Um jogo onde o usuario tenta adivinhar um numero aleatorio
    """
    
    print("Bem vindos ao nosso jogo de adivinhacao")
    
    #gerar um numero secreto entre 0 a 10
    numero_secreto = random.randint(0, 10)
    
    tentativas = 0
    
    while True:
        try:
            palpite = int(input("Digite seu palpite: "))
            tentativas += 1
            
            if palpite < numero_secreto:
                print("Muito abiaxo do numero secreto")
            elif palpite > numero_secreto:
                print("Muito acima do numero secreto")
            else:
                print(f"Parabens vc acertou: o numero era {numero_secreto}, suas tentativas {tentativas} restantes")
                break
        except ValueError:
            print("Por favor, digite um numero valido")
            
if __name__ == '__main__':
    jogar_adivinhacao()