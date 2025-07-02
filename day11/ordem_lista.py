#lista ordenada por meio do sorted()

# 1. lista NUMERICA

lista_num = [55, 69, 31, 66, 77, 121, 661, 1, 2, 3, 4]

#sorted() é uma funcao do python, aceita lista e a retorna em ordem
numeros_ordenados = sorted(lista_num)
numeros_ordenados2 = sorted(lista_num, reverse = True)

print(numeros_ordenados)
print(numeros_ordenados2)