def calcular_imc():
    """
    Funcao que calcula o IMC
    """
    
    print("Bem vindo a calculadora de IMC")
    
    try:
        peso = float(input("Digite o seu peso em quilogramas: "))
        
        altura = float(input("Digite a sua altura em metros: "))
        
        if peso < 0 or altura < 0:
            print("O peso e altuea deve ser maio que 0")
            return #encerrar a funcao
        imc = round(peso / (altura ** 2), 2)
        
        if imc < 18.5:
            print("Você está abaixo do peso ideal")
        elif 18.5 <= imc < 24.9:
            print("Você está no peso normal")
        elif 25 <= imc < 29.9:
            print("Você está de sobrepeso")
        else:
            print("Você está com obesidade")
            
    except ValueError:
        print("A entrada está invalida")
    
    #significa que estamos rodando esse codigo internamente
    #apenas roda se eu rodat o meu script calcular_imc    
if __name__ == "__main__":
    calcular_imc()
    
                    