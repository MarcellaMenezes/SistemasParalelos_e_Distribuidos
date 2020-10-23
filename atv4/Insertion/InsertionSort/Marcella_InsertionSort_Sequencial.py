import random
import time

def insertionSort(vet,size):
    for i in range(size):
        valor = vet[i]

        while i > 0 and vet[i - 1] > valor:
            vet[i] = vet[i - 1]
            i -= 1

        vet[i] = valor
        

if __name__ == '__main__':  
    vet = []
    size = 10000
    for i in range(size):
         vet.append(random.randint(0,size))

    inicio = time.time()    
    insertionSort(vet, size)
    fim = time.time()
    print vet

    print("\nTempo de inicializacao: "+str(inicio)+"\nTempo de Finizalizacao: "+str(fim) + "\nTempo de Execucao: "+ str(fim-inicio))
