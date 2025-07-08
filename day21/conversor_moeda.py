def conversor_moeda(valor, taxa_cambio, tipo_conversao):
    """
    Essa fincao converte dolar em reais e vice e versa
        
    Args: 
        valor: (float): Valor a ser convertido (monetario)
        taxa_cambio: A taxa de cambio atual
        tipo_conversao: dolar para real e real para dolar
    
    Return:
        float: O valor convertido, arredondado para duas casas decimais
        
    Raises:
        ValueError: Se o tipo de conversao for errado
    """
    
    if tipo_conversao == 'dolar_real':
        return round(valor * taxa_cambio, 2)
    elif tipo_conversao == 'real_dolar':
        return round(valor / taxa_cambio, 2)
    else:
        return ValueError("Tipo de coversão inválida")

print(conversor_moeda(12, 5.43, 'dolar'))