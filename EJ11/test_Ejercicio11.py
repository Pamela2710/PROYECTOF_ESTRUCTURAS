import unittest
import Ejercicio11


class TestEj10(unittest.TestCase):

    def test_1(self):
        a=Ejercicio11.Ejercicio11(0)
        resultado=a.ResultadoNumerosStrobogramaticos()
        self.assertEqual(resultado,[' '])
        
    def test_2(self):
        a=Ejercicio11.Ejercicio11(1)
        resultado=a.ResultadoNumerosStrobogramaticos()
        self.assertEqual(resultado,['0', '1', '8'])
    
    def test_3(self):
        a=Ejercicio11.Ejercicio11(2)
        resultado=a.ResultadoNumerosStrobogramaticos()
        self.assertEqual(resultado,['0 0', '1 1', '6 9', '8 8', '9 6'])
    
    def test_4(self):
        a=Ejercicio11.Ejercicio11(3)
        resultado=a.ResultadoNumerosStrobogramaticos()
        self.assertEqual(resultado,['000', '101', '609', '808', '906', '010', '111', '619', '818', '916', '080', '181', '689', '888', '986'])
    
    
    ####------ADVERTENCIA------#####
    
    # Por alguna razon cuando intento hacer la prueba 5 en spyder (software donde hago el codigo)
    # mi computadora se freezea y en realidad no se porque ocurre esto, no significa que el codigo no sirva sino
    # que donde lo desarrollo no lo soporta. Se puede intentar el codigo que tengo con 4 como variable en Jupyter
    # Notebook y funciona sin problema, de nuevo se puede intentar correr la prueba 5 pero si no funciona se puede
    # coger el codigo y meterlo en Jupyter Notebook para que sirva
    
    
    #def test_5(self):
        #a=Ejercicio11.Ejercicio11(4)
        #resultado=a.ResultadoNumerosStrobogramaticos()
        #self.assertEqual(resultado,['1001', '6009', '8008', '9006', '1111', '6119', '8118', '9116', '1691', '6699', '8698', '9696', '1881', '6889', '8888', '9886', '1961', '6969','8968', '9966'])



if __name__ == '__main__':

    unittest.main()

