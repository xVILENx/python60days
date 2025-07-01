# lista de frutas

frutas= ["banana", "maçã", "uva", "pera", "manga"]

for fruta in frutas:
    print(fruta)
    
# Utilizando input para colocar as frutas

frutas = []

while True:
    fruta = input("Digite uma fruta: ")
    if fruta == "sair":
        break
    else:
        frutas.append(fruta)
        
print(frutas)