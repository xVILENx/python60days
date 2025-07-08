def eh_palindromo(texto):
    """

    Verificar se um número, texto ou palvra é um palíndromo ou não
    : param texto: Palavra, texto ou numero
    : return: Uma mensagem indicando se é um palíndromo ou não
    """
    
    texto = str(texto).replace(" ", "").lower()
    
    if texto == texto[::-1]:
        return f"{texto} é um palíndromo"
    return f"{texto} não é um palíndromo"
        
print(eh_palindromo("ovo"))
print(eh_palindromo("oi"))
print(eh_palindromo(123321))