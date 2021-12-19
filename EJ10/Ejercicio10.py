
# Ejercicio 10

# Basicamente se nos da un numero n y un arreglo conocido como edges cuyo cada elemento (una tupla) representan los
# nodos que se encuentran conectados, lo que se pide hacer es contar el numero de conexiones que los elementos del
# graph tiene, es decir cuantos vertices se encuentran conectados. Se tiene una funcion que se encarga de cambiar el
# valor clave o indice de los elementos en el arreglo que se dio segun su condicion en el arreglo edge. Este nuevo
# arreglo puede tener dos elementos de distinto valor pero con un indice o "key" igual por lo que se considera un unico
# elemento. La funcion de "Comparator" se encarga de que si en el nuevo arreglo existen indices diferentes la variable
# costo ira incrementando. Esto se pide que se haga en el nuevo arreglo basado en la informacion de edges, cada vez que 
# se encuentra una conexion entre dos nodos, se cambia el indice del segundo valor al del primero, se lo considera
# como un nuevo elemento y el valor o "conexion" es almacenado en un arreglo final cuya longitud nos describe el numero de 
# conexiones del graph


class Ejercicio10:
    
     def __init__(self,numero,vertice,edge):
         self.vertice=[vertice[i] for i in range(numero)]
         self.edge=[edge[i] for i in range (len(edge))]
         self.numero=numero
         self.grafico={}
         self.elemento=[]
         self.costo=0
         self.respuesta=[]
    
     def Comparador(self,indice):
         
        self.elemento.append(indice)
        
        for i in self.grafico[indice]:
            if i not in self.elemento:
                self.costo += self.Comparador(i)
                
        return self.costo
    
     
     def ComponentesConectados(self):
         valorTemporal=0
         
         for llave in self.vertice:
             self.grafico[llave]=[]
             
         for (i0,i1) in self.edge:
             self.grafico[i0].append(i1)
             self.grafico[i1].append(i0)
         self.elementos=set()
         
         for i in self.vertice:
             if i not in self.elemento:
                 valorTemporal=self.Comparador(i)
                 self.respuesta.append(valorTemporal)
                 
         return len(self.respuesta)
                 
     
#node = [0,1,2,3,4]
#tople = [[0,1],[1,2],[2,3]]

#a = Ejercicio10(len(node),node,tople)
#print(a.ComponentesConectados())
     
    
         
