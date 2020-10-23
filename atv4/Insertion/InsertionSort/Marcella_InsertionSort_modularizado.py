import random
import time

def insertionSort(vet,size):
    for i in range(size):
        valor = vet[i]

        while i > 0 and vet[i - 1] > valor:
            vet[i] = vet[i - 1]
            i -= 1

        vet[i] = valor


def adicionaValoresDeUmIntervalo(vet, vetPacote, inicio, fim):
    for elemento in vet:
        if elemento >= inicio and elemento <fim
            vetPacote.add(elemento)

        
def pacotes(vet,vet1, vet2, vet3, vet4):

    adicionaValoresDeUmIntervalo(vet, vetPacote,          0,   len(vet)/4)    # < len(vet)/4
    adicionaValoresDeUmIntervalo(vet, vetPacote, len(vet)/4,   len(vet)/2)    # >= len(vet)/4   and < len(vet)/2
    adicionaValoresDeUmIntervalo(vet, vetPacote, len(vet)/2,   len(vet)*3/4)  # >= len(vet)/2   and < len(vet)*3/4
    adicionaValoresDeUmIntervalo(vet, vetPacote, len(vet)*3/4, len(vet))      # >= len(vet)*3/4 and < len(vet)
    

def ordenaVets(vet1, vet2, vet3, vet4):
    insertionSort(vet1,len(vet1))
    insertionSort(vet2,len(vet2))
    insertionSort(vet3,len(vet3))
    insertionSort(vet4,len(vet4))


def juntarTodos(vetNovo, vet1, vet2, vet3, vet4):
     for i in vet1:
        vetNovo.append(i)
     for i in vet2:
        vetNovo.append(i)
     for i in vet3:
        vetNovo.append(i)
     for i in vet4:
        vetNovo.append(i)

    
if __name__ == '__main__':  
    vet     = []
    vet1    = []
    vet2    = []
    vet3    = []
    vet4    = []
    vetNovo = []
    size = 10000
    
    for i in range(size):
         vet.append(random.randint(0,size))

    inicio = time.time()    
    pacotes(vet, vet1, vet2, vet3, vet4)
    ordenaVets(vet1, vet2, vet3, vet4)
    juntarTodos(vetNovo, vet1, vet2, vet3, vet4)
    fim = time.time()
    print vetNovo

    print("\nTempo de inicializacao: "+str(inicio)+"\nTempo de Finizalizacao: "+str(fim) + "\nTempo de Execucao: "+ str(fim-inicio))
