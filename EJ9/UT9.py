import unittest
import Ejercicio9


class MyTestCase(unittest.TestCase):
    def test_1(self):
        Q = Ejercicio9.Node(4, None)
        P = Ejercicio9.Node(3, Q)
        O = Ejercicio9.Node(2, P)
        M = Ejercicio9.Node(7, O)
        N = Ejercicio9.Node(5, M)

        result1 = Ejercicio9.Desarrollo(N)
        D1 = result1.Insertar(6)
        self.assertEqual(D1, [5, 6, 7, 2, 3, 4])  # add assertion here

    def test_2(self):
        M = Ejercicio9.Node(2, None)
        N = Ejercicio9.Node(0, M)

        result2 = Ejercicio9.Desarrollo(N)
        D2 = result2.Insertar(1)
        self.assertEqual(D2, [0, 1, 2])  # add assertion here

    def test_3(self):

        P = Ejercicio9.Node(6, None)
        O = Ejercicio9.Node(5, P)
        M = Ejercicio9.Node(17, O)
        N = Ejercicio9.Node(8, M)

        result3 = Ejercicio9.Desarrollo(N)
        D3 = result3.Insertar(8)
        self.assertEqual(D3, [8, 8, 17, 5, 6])  # add assertion here

    def test_4(self):

        N = Ejercicio9.Node(1, None)

        result4 = Ejercicio9.Desarrollo(N)
        D4 = result4.Insertar(0)
        self.assertEqual(D4, [1, 0])  # add assertion here

    def test_5(self):

        M = Ejercicio9.Node(34, None)
        N = Ejercicio9.Node(0, M)
        result5 = Ejercicio9.Desarrollo(N)
        D5 = result5.Insertar(-10)
        self.assertEqual(D5, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
