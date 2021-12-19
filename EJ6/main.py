##-------- EJERCICIO 6 ---------

# En este caso, el ejercicio nos da un arreglo donde tenemos un tamaño determinado. Lo que nos pide este ejercicio es crear sub-arreglos,
# partiendo del arreglo inicial y posteriormente obtener las sumas que sean impares. Lo que se hizo en este ejercicio es determinar el tamaño del arreglo,
# de tal forma que podamos saber hasta donde se tienen que formar sub-arreglos. Se crea una variable posicion la cual recorrera todo el arreglo y posteriormente se
# obtendrá la suma de cada sub-arreglo generado, de tal manera que, esta suma, se añada a un nuevo arreglo con todas las sumas impares.


import unittest


def TestValue_results():
    #---Ejercicios del proyecto---
    assert calculoEjercicio6([1, 3, 5]) == 4, "Should be: 4"
    assert calculoEjercicio6([2, 4, 6]) == 0, "Should be: 0"

    #---Ejercicios propios---
    assert calculoEjercicio6([1, 7, 4, 8, 9]) == 8, "Should be: 8"
    assert calculoEjercicio6([0, 1, 8]) == 4, "Should be: 4"
    assert calculoEjercicio6([9, 4, 7, 2]) == 6, "Should be: 6"

def calculoEjercicio6(arr):
    impares = 0
    for posicion in range(len(arr)):
        subArreglo = []
        tamanioSubArr = 0
        suma = 0
        while posicion + tamanioSubArr < len(arr):
            suma += arr[posicion + tamanioSubArr]
            subArreglo.append(suma)
            tamanioSubArr += 1
        #print(subArreglo) si se desea ver los sub arreglos que se forma, quitar le comentario

        for i in range(len(subArreglo)):

            if subArreglo[i] % 2 != 0:
                impares += 1
    return impares

def main():
    print("---Ejercicios del proyecto---")
    print("Output: " , calculoEjercicio6([1, 3, 5]))
    print("Output: ", calculoEjercicio6([2,4,6]))

    print("---Ejercicios propios---")
    print("Output" , calculoEjercicio6([1, 7, 4, 8, 9]))
    print("Output", calculoEjercicio6([0, 1, 8]))
    print("Output: ", calculoEjercicio6([9, 4, 7, 2]))
    return 0


if __name__ == "__main__":
    main()
    TestValue_results()
    print("All test cases passed")
