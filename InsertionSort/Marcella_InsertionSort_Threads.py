import random
import time
import threading

def insertionSort(vet,size):
    for i in range(size):
        valor = vet[i]

        while i > 0 and vet[i - 1] > valor:
            vet[i] = vet[i - 1]
            i -= 1

        vet[i] = valor


def adicionaValoresDeUmIntervalo(vet, vetPacote, inicio, fim):
    for elemento in vet:
        if elemento >= inicio and elemento <fim:
            vetPacote.append(elemento)

        
def pacotes(vet,vet1, vet2, vet3, vet4):
    
    t1 = threading.Thread(target = adicionaValoresDeUmIntervalo, args = (vet, vet1,          0,   len(vet)/4))    # < len(vet)/4
    t1.start()                       
    t2 = threading.Thread(target = adicionaValoresDeUmIntervalo, args = (vet, vet2, len(vet)/4,   len(vet)/2))    # >= len(vet)/4   and < len(vet)/2
    t2.start()                    
    t3 = threading.Thread(target = adicionaValoresDeUmIntervalo, args = (vet, vet3, len(vet)/2,   len(vet)*3/4))  # >= len(vet)/2   and < len(vet)*3/4
    t3.start()
    t4 = threading.Thread(target = adicionaValoresDeUmIntervalo, args = (vet, vet4, len(vet)*3/4, len(vet)))      # >= len(vet)*3/4 and < len(vet)
    t4.start()


def juntarTodos(vetNovo, vet1, vet2, vet3, vet4):
     for i in vet1:
        vetNovo.append(i)
     for i in vet2:
        vetNovo.append(i)
     for i in vet3:
        vetNovo.append(i)
     for i in vet4:
        vetNovo.append(i)
        

def ordenaVets(vet1, vet2, vet3, vet4):
    t1 = threading.Thread(target = insertionSort, args = (vet1,len(vet1)))
    t1.start()
    t2 = threading.Thread(target = insertionSort, args = (vet2,len(vet2)))
    t2.start()
    t3 = threading.Thread(target = insertionSort, args = (vet3,len(vet3)))
    t3.start()
    t4 = threading.Thread(target = insertionSort, args = (vet4,len(vet4)))
    t4.start()

    
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
