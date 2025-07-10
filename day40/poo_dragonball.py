class PersonagemDB:
    # O self garante que cada instancia da classe tenha seus proprios valores unicos sem interferir nas outras classes
    def __init__(self, nome, poder, nivel, transformacao="Base"):
        """
        Inicializa os atributos do personagem
        self garante que esses atributos sejam unicos para o personagem
        """
        
        self.nome = nome  
        self.poder = poder
        self.nivel = nivel
        self.transformacao = transformacao
        
    # o 'self' é usado para acessar e exibir os atributos do objeto atual.
    def exibir_informacoes(self):
        """
        Exibe informacoes do personagem
        """
        
        print(f"Nome: {self.nome}")
        print(f"Poder: {self.poder}")
        print(f"Nivel: {self.nivel}")
        print(f"Tranformacao: {self.transformacao}")
        
    def treinar(self, horas):
        """
        Aumenta o poder do personagem com base nas horas treinadas
        """
        
        aumento = horas * 10
        self.poder += aumento
        print(f"{self.nome} treinou por {horas} horas e aumentou seu poder em {aumento}")
    
    def transformar(self, nova_transformacao):
        """ 
        Muda a transformacao do personagem
        """
        
        self.transformacao = nova_transformacao
        print(f"{self.nome} se transformou em {nova_transformacao}")
        
goku = PersonagemDB(nome="Goku", poder = 9000, nivel="Super Saiyajin")

goku.exibir_informacoes()       

vegeta = PersonagemDB(nome="Vegeta", poder = 8500, nivel="Saiyajin")
vegeta.treinar(horas=10)
vegeta.transformar(nova_transformacao="Super Saiyajin")
vegeta.exibir_informacoes()