import re

def validar_email(email):
    """
    Função recebe email e valida por meio do regex
    
    Args: email para validação
    """
    
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(regex, email):
        print(f" {email} - Email valido.")
    else:
        print(f" {email} - Email invalido.")
        
 # ^ indica o inicio do texto     
 # [a-zA-Z0-9_.+-]
 # @ Simbolo obrigatorio de um email  
 # +\. 
 # $ finaliza o texto
 
validar_email("vi@hotgmail.com")
validar_email("kahskjkldi.com")