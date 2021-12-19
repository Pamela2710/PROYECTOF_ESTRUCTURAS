##--- EJERCICIO 4 ----

# En este ejercicio, tenemos un dado de 6 lados que es lanzado un numero m determinado de veces, un numero n de veces que el dado es lanzado, el valor que se obtuvo del dado,
# se perdió, sin embargo, tenemos el promedio de la suma que da los valores obtenidos de cada lanzada y tambien tenemos los numeros que se obtuvieron y que no se perdieron.
# Por lo que para resolver para resolver este ejercicio, se debe obtener la suma total con la ayuda del promedio y el numero de veces que se perdieron los datos.
# Posteriormente se hacen calculso aritmeticos para determinar si las divisiones son pares o impares y con la ayuda del residuo, podremos saber que numeros son los que se perdieron.
# Hay que tomar en cuenta que si tenemos un numero determinado de tiradas y lo multiplicamos por el numero de lados que tiene el dado, la suma no puede ser mayor a este numero, sino sería un error de bordes.


import unittest


def TestValue_results():
    #Ejemplos proyecto
    assert calculoEjercicio4([3, 2, 4, 3], 4, 2) == [6, 6], "Should be: [6, 6]"
    assert calculoEjercicio4([1, 5, 6], 3, 4) == [3, 2, 2, 2], "Should be: [3, 2, 2, 2]"

    #Ejemplos propios
    assert calculoEjercicio4([6, 6, 5, 3], 4, 4) == [3, 3, 3, 3], "Should be: [3, 3, 3, 3]"
    assert calculoEjercicio4([1], 2, 1) == [3], "Should be: [3]"
    assert calculoEjercicio4([1, 2], 3, 2) == [5, 4], "Should be: [5, 4]"



def calculoEjercicio4(roll, mean, n):
    m = len(roll)  #tamanio arreglo incompleto

    totalValores = n + m  #valores del arreglo completo
    sumaTotal = mean * totalValores #Suma que nos ayudara a obtener el promedio

    sumaArreglo = sum(roll) # Suma del arreglo incompleto
    sumaNumerosFaltantes = sumaTotal - sumaArreglo #Suma de los numeros que faltan en el arreglo

    divsionConResiduo = sumaNumerosFaltantes // n  #Obtenemos el residuo de la division
    residuo = sumaNumerosFaltantes % n
    arrValoresEncontrados = [] # Arreglo para anadir los numeros perdidos

    for i in range(n):

        numeroFinal = divsionConResiduo
        if residuo > 0:
            numeroFinal += 1
            residuo -= 1
        arrValoresEncontrados.append(numeroFinal)
    return arrValoresEncontrados


def main():
    print("---Ejercicios del proyecto---")
    print("Output: ",  calculoEjercicio4([3, 2, 4, 3], 4, 2))
    print("Output: ", calculoEjercicio4([1, 5, 6], 3, 4))

    print("---Ejercicios propios---")
    print("Output: ", calculoEjercicio4([6, 6, 5, 3], 4, 4))
    print("Output: ", calculoEjercicio4([1], 2, 1))
    print("Output: ", calculoEjercicio4([1, 2], 3, 2))



if __name__ == "__main__":
    main()
    TestValue_results()
    print("All test cases passed")
