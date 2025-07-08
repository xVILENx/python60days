def anagrama(palavra1, palavra2):
    """

    Verificar se duas palavras sao um anagrama ou não
    : param palavra1: Primeira palavra
    : param palavra2: Segunda palvra
    : return: True se as palvras forem um anagrama
    """
    
    # removendo espaços e covertendo para letras minúsculas
    palavra1 = palavra1.replace(" ", "").lower()
    palavra2 = palavra2.replace(" ", "").lower()
    
    if sorted(palavra1) == sorted(palavra2):
        return f"Essas palavras sao anagramas"
    return f"Essas palavras nao sao anagramas"

print(anagrama("amor", "roma"))
