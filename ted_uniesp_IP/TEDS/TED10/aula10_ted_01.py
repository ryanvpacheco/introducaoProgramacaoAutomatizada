# Faça um algoritmo para ler 20 números e armazenar em um vetor. 
# Após a leitura total dos 20 números, o algoritmo deve escrever esses 20 números lidos na ordem inversa.
import random
lista = []
for i in range(0,21):
            i = random.randint(0,100)
            lista.append(i) 

lista.reverse()
print(lista)    
