from  random import randint
import numpy as np

tam = 10
tam2 = 1
m = [0]*tam
#matriz pra letra b
matriz = []
print("#"*100)
print("Matriz Primaria : ")
print("#"*100)
for y in range(tam2):
       for i in range(tam):
              m[i] = [0]*tam
       for i in range(tam):
              for j in range(tam):
                     m[i][j] = randint(1, 101)
                     
       for i in range(tam):
              print(m[i])
              
              matrizb=  np.array(m[i])
              soma2 = (m[i]* 3) 
       for x in range(m[i][j]):
              soma3 = sum(m[j] + m[i])
print("#"*100)
print("A soma dos valores internos da matriz Primaria é :",soma3)
print("#"*100)
print("Nova Matriz A :")
print("#"*100)
for linha in range(10):
    linha = []

    for coluna in range(10):
        linha.append(randint(1, 101))

    matriz.append(linha)

for linha_matriz in matriz:
    print(linha_matriz)


print("#"*100)
matrizb = np.array(matriz)
soma = matrizb* 3
print("A mutiplicação dos numeros da matriz A")
print("Resulta na matriz B:")
print("#"*100)
print(soma)
print("#"*100)
print("FIM DO PROGRAMA !")