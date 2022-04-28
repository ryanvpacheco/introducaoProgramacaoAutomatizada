import random
import numpy as np

matriz= []
print("#"*100)
print("MATRIZ 10X10 A :")
print("#"*100)
for x in range(1, 11):
    lista_auxiliar = []
    for y in range(1, 11):
        lista_auxiliar.append(random.randint(1, 100))
    matriz.append(lista_auxiliar)
    print(lista_auxiliar)
soma = []
soma.append(matriz)
print("#"*100)
print("Soma dos indices da matriz : ")
print(np.sum(soma))

print("#"*100)
matrizb = np.array(matriz)
soma = matrizb* 3
print("A mutiplicação dos numeros da matriz A")
print("Resulta na matriz B:")
print("#"*100)
print(soma)
print("#"*100)
print("FIM DO PROGRAMA")
print("#"*100)