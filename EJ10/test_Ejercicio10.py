import unittest
import Ejercicio10


class TestEj10(unittest.TestCase):

    def test_1(self):
        node = [0,1,2,3,4]
        tople = [[0,1],[1,2],[3,4]]
        a = Ejercicio10.Ejercicio10(len(node),node,tople)
        resultado=a.ComponentesConectados()
        self.assertEqual(resultado,2)
        
    def test_2(self):
        node = [0,1,2,3,4]
        tople = [[0,1],[1,2],[2,3],[3,4]]
        a = Ejercicio10.Ejercicio10(len(node),node,tople)
        resultado=a.ComponentesConectados()
        self.assertEqual(resultado,1)
    
    def test_3(self):
        node = [0,1,2,3,4,5,6,7,8,9,10]
        tople = [[0,1],[1,2],[2,3],[3,4]]
        a = Ejercicio10.Ejercicio10(len(node),node,tople)
        resultado=a.ComponentesConectados()
        self.assertEqual(resultado,7)
        
    def test_4(self):
        node = [0,1,2,3,4,5,6,7,8]
        tople = [[0,1],[1,2],[2,3],[3,4],[5,7],[6,8]]
        a = Ejercicio10.Ejercicio10(len(node),node,tople)
        resultado=a.ComponentesConectados()
        self.assertEqual(resultado,3)
    
    def test_5(self):
        node = [0,1,2,3,4,5,6,7,8]
        tople = [[0,1],[1,2],[2,3],[3,4],[5,7],[5,6],[6,8]]
        a = Ejercicio10.Ejercicio10(len(node),node,tople)
        resultado=a.ComponentesConectados()
        self.assertEqual(resultado,2)



if __name__ == '__main__':

    unittest.main()

