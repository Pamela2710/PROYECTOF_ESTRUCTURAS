## EJERCICIO 5--------------------

# En este ejercicio, hay que determinar el ganador de un juego de fibonacci, donde la persona que llegue a la raiz del arbol es la que pierde.
# En este caso, para resolver el ejercicio, usé recursion ya que es una llamada constante para determinar el numero de nodos que se encuentra en el arbol,
# para determinar el ganador, fue sencillo, calculé el numero de nodos que tiene todo el arbol, dependiendo de la raiz, de tal manera que si, el arbol tiene
# un número par de nodos, el ganador será Alice y si el arbol, tiene un numero impar de nodos, el ganador sera Bob.


import unittest


def TestValue_results():
    # Ejemplo del proyecto
    assert ganador(3) == True, "Should be: True"

    # Ejemplos propios
    assert ganador(4) == False, "Should be: False"
    assert ganador(6) == True, "Should be: True"
    assert ganador(1) == False, "Should be: False"
    assert ganador(2) == True, "Should be: True"


def order(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0

    numNodos = 1 + order(n - 1) + order(n - 2)
    return numNodos


def ganador(n):
    numNodos = order(n)
    if numNodos % 2 == 0:
        return True
    else:
        return False


def main():
    print("---Ejercicio del proyecto---")
    print("Output: ", ganador(3))

    print("---Ejercicios propios---")
    print("Output: ", ganador(4))
    print("Output: ", ganador(6))
    print("Output: ", ganador(1))
    print("Output: ", ganador(2))


    return 0


if __name__ == "__main__":
    main()
    TestValue_results()
    print("All test cases passed")
