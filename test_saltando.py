import unittest
from saltando import saltos

class TestSaltos(unittest.TestCase):

    def test_1(self):
        l = [1, 1, 2, 2]
        self.assertTrue(saltos(l))

    def test_2(self):
        l = [3, 2, 1, 0, 4]
        self.assertFalse(saltos(l))

    def test_3(self):
        l = [1, 2, 0, 0]
        self.assertTrue(saltos(l))

    def test_4(self):
        l = [0]
        self.assertTrue(saltos(l))

    def test_5(self):
        l = [1, 0, 0, 0]
        self.assertFalse(saltos(l))

    def test_6(self):
        # Caso de lista vacía
        l = []
        self.assertTrue(saltos(l))

    def test_7(self):
        l = [0, 0, 0]
        self.assertFalse(saltos(l))

    def test_8(self):
        l = [5, 0, 0, 0, 0, 0]
        self.assertTrue(saltos(l))

    def test_9(self):
        l = [3, 3, 1, 2, 0, 1]
        self.assertTrue(saltos(l))

if __name__ == '__main__':
    unittest.main()
