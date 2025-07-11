class Ninja:
    def __init__(self, nome, chakra):
        self.nome = nome
        self.chakra = chakra
    
    def usar_jutsu(self, custo_chakra):
        try:
            if custo_chakra > self.chakra:
                raise ValueError("Chakra insuficiente.")
            self.chakra -= custo_chakra
            print(f"{self.nome} usou o jutsu com sucesso")
        except ValueError as Error:
            print(f"Erro: {Error} foi detectado. O {self.nome} precisar recuperar seu chakra.")
            
if __name__ == "__main__":
    naruto = Ninja(nome = "Kakashi", chakra=50)
    naruto.usar_jutsu(100)