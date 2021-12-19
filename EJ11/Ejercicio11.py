# Ejercicio 11

# Lo que se pide del ejercicio es un valor n cualquiera, lo que esto hara es que nos da todos los numeros 
# strobogramaticos (que se ven igual si se rota a 180°). Es sencillo, si se da un valor 0 se genera un arreglo vacio
# si se da un "1" se genera un arreglo de valores de un solo digito que se parecen igual al rotarse a 180°. lo que
# ira sucediendo es que si se entrega un valor igual o mayor a dos se genera un arreglo cuyos bordes definidos ya
# son numeros strobogramaticos pero con un valor en medio. Este valor de en medio ira aumentan para dar la ilusion de
# que se tiene un numero estroborgramatico. Es decir si le damos un 3 entonces cargara a este valor de en medio con uno
# de los numeros de un digito que son estrobogramaticos, si fuera 4 se aumenta el valor de en medio a dos digitos.
# Siempre son -2 al valor original que se le de y estos numeros en si seran estrobogramaticos debido a la recursion de la
# misma operacion para definir estos valores. Las estructuras de datos empleadas en si es una lista a la cual se le dan
# mas valores segun el numero de posibles numeros strobogramaticos este disponible


class Ejercicio11:
    
    def __init__(self,Numero_de_input=0,valor=0):
        self.Numero_de_input=Numero_de_input
        self.solucion=[]
        self.valor=valor
        self.valorTemporal=0
    
    def NumeroStrobogramatico(self,val):
        
        if not val:
            return [" "]
    
        if val == 1:
            return ["0","1","8"]
        self.valorTemporal=self.NumeroStrobogramatico(val-2)
        
        if not self.valorTemporal:
            self.valorTemporal.append(" ")
            
        for i in self.valorTemporal:
            if val != self.NumeroStrobogramatico:
                self.solucion.append("0"+ i +"0")
            Casos = [("1"+i+"1"), ("6"+i+"9"), ("8"+i+"8"), ("9"+i+"6")]
            self.solucion.extend(Casos)
        
        return self.solucion
    
    def ResultadoNumerosStrobogramaticos(self):
        return self.NumeroStrobogramatico(self.Numero_de_input)
        

#a=Ejercicio11(3)
#print(a.ResultadoNumerosStrobogramaticos())
    
    
    

        

