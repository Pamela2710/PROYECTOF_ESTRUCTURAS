# Ejercicio 12

# Basicamente se nos pedia que con un determinado arreglo que se entregara (que representa un arbol binario), se
# puidera hacer un recorrido de forma vertical a los elementos. Se refiere a que cada nodo del arbol esta situado en 
# una posicion vertical o columnas con un determinado valor, uno o mas elemntos actuarian en conjunto si se encuentran
# en una misma columna como el valor de la raiz y otros nodos que estuvieran en la misma posicion. Esta funcion
# logra en si tomar los valores que se dan del arreglo representando un arbol  binario y logra reorganizar los mismos
# en un nuevo arreglo pero cambiando sus posiciones. Sin embargo, en este caso no se logra que se haga una Vertical
# traversal por cada uno de los nodos si no que lo haria mas en concordancia con la "PostOrder Transversal" la cual
# va primero al valor de la izquierda, luego al de la derecha y al final al de la raiz y se entrega un nuevo arreglo
# con las posiciones originales cambiadas para representar este proceso. En si se puede interpretar a los objetos del
# del arreglo como nodos y cambiar su orden pero no se pudo realizar esta accion basandonos en su posicion vertical.
# basicamente aqui se usa una double linked list debido al hecho que estamos utilizando los elementos de nodo como val
# left y right. De igual manera se hace recursion para definir los valores de left y right y en si la posicion de los mismos
# en el nuevo arreglo. De cierta manera, esto fue lo mejor que se pudo obtener en intentar hacer que se reconozca la posicion
# vertical y bueno se espera que al menos se obtenga algo de este ejercicio

import sys
sys.setrecursionlimit(100000)

class Node:
    
    def __init__(self,valor=0,izquierda=None,derecha=None):
        self.valor=valor
        self.izquierda=izquierda
        self.derecha=derecha
        self.arregloSolucion=[]
    
    def VerticalTraversal(self,valor1,indice):
        if indice < len(valor1):
            if valor1[indice]==None:
                return []
            
            elemento=Node()
            nuevo_indice = 2*indice
            
            elemento.left=self.VerticalTraversal(valor1,nuevo_indice+1)
            elemento.valor=valor1[indice]
            elemento.right=self.VerticalTraversal(valor1,nuevo_indice+2)
            
            nuevamatriz=[(elemento.valor)]
            self.arregloSolucion.append(nuevamatriz)
        
        return self.arregloSolucion
                
        
lista = [20,30,43,12,2,1,0,81]
raiz=Node()
print(raiz.VerticalTraversal(lista,0))  
    
   
        
        

            
    
    


