#En el siguiente ejercicio se construye una lista enlazada circular ordenada, en la cual se insertara un nuevo valor
#el mismo sera insertado en la posicion correcta de manera que se cumpla un orden, para este programa se utilizaron dos
#clases, la primera que es para la creacion de nodos y la segunda que realiza el proceso de insertar el nuevo nodo,
#en la clase desarrollo se inicializa con la lista enlazada y despues se dirige a la funcion insertar donde entra
#como parametro un valor entero que se convertira en nodo, cuando se termine el proceso de insertar la lista enlazada
#se dirige a la funcion linkedList_List en donde se transformara la lista enlazada a una lista normal para poder retornar
#el resultado final y poder realizar los Unit test.

class Node(object):
    def __init__(self, valor, next=None):
        self.valor = valor
        self.next = next

#Clase Desarrollo que se inicializa con la lista enlazada
class Desarrollo(object):
    def __init__(self, head):
        self.head = head

    #Funcion de conversion de lista enlazada a lista
    def linkedList_List(self, head):
        if not head:
            return []
        pointer = head
        listn = []
        while pointer:
            #Ingreso de nodos a la lista listn
            listn.append(pointer.valor)
            pointer = pointer.next
        #Resultado final
        return listn

    #Funcion que inserta el valor entero a la lista enlazada
    def Insertar(self, nuevo):
        Valc = self.head
        Vald = self.head.next

        if nuevo < 0:
            print("No se aceptan valores negativos")
            return False

        #Si la cabeza es nula
        if self.head is None:
            self.head = Node(nuevo)
            self.head.next = self.head

        else:
            while Vald is Valc:
                #Condiciones para insertar el valor
                if Valc.valor > Vald.valor:
                    if nuevo >= Valc.valor or nuevo <= Vald.valor:
                        Vald = Node(nuevo, Vald)

                if Valc.valor < Vald.valor:
                    if Valc.valor <= nuevo <= Vald.valor:
                        Vald = Node(nuevo, Vald)

                if Vald == self.head:
                    Vald = Node(nuevo, self.head)

            Valc.next = Node(nuevo, Vald)
            #Llamado a la funcion de conversion de la lista enlazada
            A = self.linkedList_List(self.head)
            return A
'''
a = Node(0, Node(2, None))
lista = Desarrollo(a)
b=lista.Insertar(1)
print(b)
'''