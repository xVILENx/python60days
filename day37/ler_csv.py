import pandas as pd

def main():
    nome_arquivo = "test.csv"
    
    df = pd.read_csv(nome_arquivo)
    
    print(df)
    
    # informacoes das 5 primeiras linhas sobre o df
    print(df.head())
    # pega informacoes do df
    print(df.info())
    
    #exibi o formato do df
    print(df.shape)
    
if __name__ == "__main__":
    main()