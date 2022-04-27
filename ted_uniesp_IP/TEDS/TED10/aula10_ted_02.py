# Faça um algoritmo para ler 50 números e armazenar em um vetor VET, 
# verificar e escrever se existem números repetidos no vetor VET e em que posições se encontram.



# for i in lista:
#     print(i, end=',')
#     print(lista.count(i))
    

from collections import defaultdict
import random
chaves = defaultdict(list)
lista = [] 

numeroUm = int(input("Digite um numero : "))
numeroDois = int(input("Digite um numero : "))

try:
        for i in range(0,50):
            i = random.randint(numeroUm , numeroDois)
            lista.append(i) 
        print(lista)
        print("#"* 150)
        print("Deseja localizar os numeros repetidos ? ")
        simenao = input("(s)im ou (n)ão :")
        letraMaiuscula = simenao.upper()
        print("#"* 150)
        if simenao == "S" or "s":
            for chave, i in enumerate(lista):
                chaves[i].append(chave)

            for i in chaves:
                if len(chaves[i]) > 1:
                    print(f'O numero {i} se repete nos indecis {chaves[i]}')
                    
            print("#"* 150)
            print("Programa Finalizado")
        else :
            print("Programa encerrado")
            
            
except :
    print("ERR00")
    print("O programa aceita somente numeros inteiros e em ordem crescente!")

