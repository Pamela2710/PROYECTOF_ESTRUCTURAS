from collections import defaultdict

#En el codigo a continuacion se resuelve el caso de contar el numero de subsecuencias que genera un arreglo,
#en este caso se dio como entrada un arreglo de la dimension deseada controlando que el tamaño del mismo sea
#mayor a 3, se utilizó el defaultdict porque facilita el acceso a diccionarios, como al inicio no se utilizan
#diccionarios esto permite que el programa no genere errores mas bien genere entradas en cada posicion del,
#arreglo doubleElem, estos van a tener un parametro tipo entero para que despues se puedan guardar cada uno
#de los valores de la secuencia en formato clave y valor es decir en un bucket de doubElem va a haber
#defauldict(parametro int, {k:v}) k serán los valores de la secuencia y el value será 1.
class Subseq:
    def __init__(self, sec, da=[], dp=[]):
        self.secuencia = sec
        self.doubElem = da
        self.doubElem_ = dp

    def desarrollo(self):
        total = 0
        elem = len(self.secuencia)
        if elem < 3:
            return False
        #Asignación de defaultdict a cada bucket de los arreglos
        for i in range(elem):
            self.doubElem.append(defaultdict(int))

        for i in range(elem):
            self.doubElem_.append(defaultdict(int))
        #Iteracion del arreglo secuencia en fila'columna desde i¿1 y j¿0 primera asignacion del valor dado al defaultdict
        #en el bucket 1 que esta en el arreglo doubElem
        for i in range(1, elem):
            for j in range(i):
                self.doubElem[i][self.secuencia[i] - self.secuencia[j]] += 1

        self.doubElem_[0] = self.doubElem_[1] = {}
        #Subsecuencias
        for i in range(2, elem):
            for j in range(i):
                k = self.secuencia[i] - self.secuencia[j]

                if k in self.doubElem[j]:
                    self.doubElem_[i][k] += self.doubElem[j][k]
                    total += self.doubElem[j][k]

                if k in self.doubElem_[j]:
                    self.doubElem_[i][k] += self.doubElem_[j][k]
                    total += self.doubElem_[j][k]

        return total

'''
n = int(input("Tamaño de la lista:"))
nums = []
for x in range(n):
    valor = int(input("Ingrese valor entero: "))
    nums.append(valor)
print(nums)
D = Subseq(nums)
print(D.desarrollo())
'''
