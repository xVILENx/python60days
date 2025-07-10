import json
from typing import Any

def salvar_dados(arquivo: str, dados: Any) -> None:
    """ 
    Salvar os dados fornecidos em formato JSON
    
    :param: arquivo: Caminho para o arquivo JOSN
    :param dados: Os dados que srao armazenados no arquivo
    """
    
    with open(arquivo, 'w', encoding= "utf-8") as f:
              json.dump(dados, f, indent=4, ensure_ascii=False)
              
def carregar_dados(arquivo: str) -> Any:
    """ 
    Le os dados do arquivo JSON
    
    :param: arquivo: Caminho para o arquivo JOSN
    :return: Dados carregador e lidos do arquivo JSON
    """
    
    try: 
        with open(arquivo, 'r', encoding="utf-8") as f:
            return json.load(f)
    except FileExistsError:
        print("O aquivo nao foi encontrado, caminho do arquivo {arquvio}")
        return {}
    
dados_exemplo = {"nome": "Vilen", "cidade": "Sao Paulo", "cargo": "Programador"}   

nome_arquivo = "nome_vilen.json"

salvar_dados(nome_arquivo, dados_exemplo)

dados_carregados = carregar_dados(nome_arquivo)

print("Dados carregados: ", dados_carregados)
    