numero = int(input("Digite um numero para ver se ele é primo: "))

# assumimos como true primeiramente uma variavel como primo

eh_primo = True

if numero <= 1:
    eh_primo = False
    
for i in range(2, int(numero ** 0.5) + 1):
    if numero % i == 0:   # Se o numero for divisivel por 1
        eh_primo = False   # Não é primo
        break   # Saimos do loop, pois já encontramos um divisor
    
if eh_primo:
    print(f"{numero} eh numero primo")
else:
    print(f"{numero} nao eh um umero primo")
    