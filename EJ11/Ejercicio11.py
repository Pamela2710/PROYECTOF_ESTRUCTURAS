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
    
    
    

        

