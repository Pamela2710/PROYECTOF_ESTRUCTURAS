import unittest
import Ejercicio12

class TestEj12(unittest.TestCase):

    def test_1(self):
        lista = [3,9,20,None,None,15,7]
        raiz=Ejercicio12.Node()
        resultado=raiz.VerticalTraversal(lista,0)  
        self.assertEqual(resultado,[[9], [15], [7], [20], [3]])
    
    def test_2(self):
        lista = [3,9,8,4,0,1,7]
        raiz=Ejercicio12.Node()
        resultado=raiz.VerticalTraversal(lista,0)  
        self.assertEqual(resultado,[[4], [0], [9], [1], [7], [8], [3]])
    
    def test_3(self):
        lista = [3,9,8,4,0,1,7,None,None,None,2,5]
        raiz=Ejercicio12.Node()
        resultado=raiz.VerticalTraversal(lista,0)  
        self.assertEqual(resultado,[[4], [2], [0], [9], [5], [1], [7], [8], [3]])
    
    def test_4(self):
        lista = [9,6,5,6,3,None,1,2]
        raiz=Ejercicio12.Node()
        resultado=raiz.VerticalTraversal(lista,0)  
        self.assertEqual(resultado,[[2], [6], [3], [6], [1], [5], [9]])
    
    def test_5(self):
        lista = [20,30,43,12,2,1,0,81]
        raiz=Ejercicio12.Node()
        resultado=raiz.VerticalTraversal(lista,0)  
        self.assertEqual(resultado,[[81], [12], [2], [30], [1], [0], [43], [20]])
    
    

if __name__ == '__main__':

    unittest.main()


