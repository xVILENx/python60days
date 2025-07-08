fibonacci = [0, 1] # A sequência sempre começa com 0 e 1

#só 8 pq seram só 10 numeros
for i in range(8):
    proximo_numero = fibonacci[-1] + fibonacci[-2] # -1 e -2 são os numeros 1 e 0 da lista
    fibonacci.append(proximo_numero)
    
print(fibonacci) #sequencia