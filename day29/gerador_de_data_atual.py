from datetime import datetime
import pytz

def exibir_data_hora_atual():
    """
    Exibe data e hora atual do sistema
    """  
    
    fuso_horario = pytz.timezone("America/Sao_Paulo")
    
    data_hora = datetime.now(fuso_horario)
    
    formato_data = data_hora.strftime("%d/%m/%y %H:%M:%S")
    
    print(f"Data e hora atual: {formato_data}")
    
if __name__ == "__main__":
    exibir_data_hora_atual()
