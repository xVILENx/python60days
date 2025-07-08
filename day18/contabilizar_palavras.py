def contar_palavras(texto):
    """

    Contear palavrs em uma string
    : param texto: String de entrada
    : return: Numero de palavras
    """
    
    # Vai separar as palvras usando o espaço
    palavras = texto.split()
    
    return len(palavras)

print(contar_palavras("oi tudo bem, como vai vc"))

texto = "oi tudo bem, como vai vc?"
palavras = texto.split()
print(palavras)