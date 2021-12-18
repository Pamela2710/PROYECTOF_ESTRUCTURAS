import unittest
import Ejercicio8


class MyTestCase(unittest.TestCase):
    def test_1(self):
        D1 = Ejercicio8.Inter([[1, 4], [2, 4], [3, 6], [4, 4]], [2, 3, 4, 5])
        result1 = D1.interMin()
        self.assertEqual(result1, [3, 3, 1, 4])  # add assertion here

    def test_2(self):
        D2 = Ejercicio8.Inter([[2, 3], [2, 5], [1, 8], [20, 25]], [2, 19, 22])
        result2 = D2.interMin()
        self.assertEqual(result2, [2, -1, 6])  # add assertion here

    def test_3(self):
        D3 = Ejercicio8.Inter([[1, 5], [4, 5], [2, 2]], [1, 3, 5])
        result3 = D3.interMin()
        self.assertEqual(result3, [5, 5, 2])  # add assertion here

    def test_4(self):
        D4 = Ejercicio8.Inter([[10, 15], [3, 8], [8, 13],[-1, 4]], [7, 0, 12, 4])
        result4 = D4.interMin()
        self.assertEqual(result4, [6, 6, 6, 6])  # add assertion here

    def test_5(self):
        D5 = Ejercicio8.Inter([[1, 5], [0, 6], [5, 7], [4, 16]], [0])
        result5 = D5.interMin()
        self.assertEqual(result5, [7])  # add assertion here


if __name__ == '__main__':
    unittest.main()
