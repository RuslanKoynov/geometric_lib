import unittest

def area(a):
    '''
    Принимает значение a(сторонa квадрата),возвращает площадь квадарата с этой стороной
    '''
    return a * a


def perimeter(a):
    '''
    Принимает значение a(сторонa квадрата),возвращает периметр квадарата с этой стороной
    '''
    return 4 * a

class SquareTest(unittest.TestCase):

    def test_area1(self):
        res = area(4)
        self.assertEqual(res, 16)

    def test_perimeter1(self):
        res = perimeter(120)
        self.assertEqual(res, 480)

    def test_area2(self):
        res = area(2.48)
        self.assertEqual(res, 6.1504)

    def test_perimeter2(self):
        res = perimeter(10,7)
        self.assertEqual(res, 42.8)

    def test_area3(self):
        with self.assertRaises(Exception):
            area(-10)

    def test_perimeter3(self):
        with self.assertRaises(Exception):
            perimeter(-5)


if __name__ == "__main__":
    unittest.ma
