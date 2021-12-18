import unittest
#En este ejercicio se resuelve de que manera entran los queries a los intervalos, es decir cada numero de la lista
#querie busca el intervalo mas apropiado, esto solo se cumple si consigue el intervalo con rango mas pequeño, en este
#ejercicio se utiliza el metodo de ordenamiento merge sort ya que la complejidad del mismo es O nlog n la clase recibe
#como entrada una matriz la cual contiene los intervalos y un arreglo de los queries, en interMin primero se realiza
#el ordenamiento del la matriz y la lista que contiene valores de los indices del tamaño de la lista de queries, va
#iterando por el bucle for

class Inter:
    def __init__(self, intervalos, queries):
        self.intervalos = intervalos
        self.queries = queries

#Metodo de ordenamiento Merge Sort
    def mergeSort(self, lista_):
        if len(lista_) <= 1:
            return
        mid = len(lista_)//2
        L = lista_[:mid]
        R = lista_[mid:]
        #Recursividad
        self.mergeSort(L)
        self.mergeSort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                lista_[k] = L[i]
                i += 1
            else:
                lista_[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            lista_[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            lista_[k] = R[j]
            j += 1
            k += 1

    def interMin(self):
        numIn = len(self.intervalos)
        numQu = len(self.queries)
        alm = []
        c = []
        for i in range(numQu):
            alm.append(i)
        #Llamado a la funcion mergeSort para ordenar ascendentemente
        self.mergeSort(alm)
        self.mergeSort(self.intervalos)

        tInterv = [0] * numQu
        j = 0
        #Recorrido de la lista alm que con tiene valores posicionales de la lista numQu
        for i in alm:
            t = self.queries[i]
            while j < numIn:
            #ingreso de los valores fila-columna de la matriz intervaloes a las variables left y right
                left = (self.intervalos[j])[0]
                right = (self.intervalos[j])[1]
                if left <= t:
                    j += 1
                    #Almacenamiento de nuevos intervalos que son resultado de la siguiente operacion aritmetica
                    #que se encarga de encontrar el tamano del intervalo
                    c.append([right - left + 1, right])
                    #ordenamiento ascendente de la matriz c
                    self.mergeSort(c)
                else:
                    break
            while c:
                #Se elimina la posicion 0 del la lista de intervalos si los valores fila-columna son < t
                if c[0][1] < t:
                    c.pop(0)
                else:
                    break
                #Caso en donde no existe el intervalo en la lista se almacena -1
            if len(c) == 0:
                tInterv[i] = -1
            else:
                tInterv[i] = c[0][0]
        return tInterv

'''
n = int(input("Tamaño filas matriz A:"))
m = int(input("Tamaño de la lista B:"))
for x in range (n):
    val1= int(input("Valor Izquierda: "))
    val2 = int(input("Valor Derecha: "))

    A.append([val1,val2])
    print(A)

for x in range (n):
    val1= int(input("Numero: "))
    B.append(val1)
'''
