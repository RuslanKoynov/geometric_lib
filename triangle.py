import unittest
def area(a, h):
    '''
    Принимает значения a(сторона треугольника) и h(высота треугольника),возвращает площадь треугольника с указанными параметрами
    '''
    return a * h / 2 

def perimeter(a, b, c): 
    '''
    Принимает значения a,b,c- стороны треугольника,возвращает периметр треугольника с указзанными параметрами
    '''
    return a + b + c

class TriangleTest(unittest.TestCase):

    def test_area1(self):
        res = area(4,10)
        self.assertEqual(res, 20)

    def test_perimeter1(self):
        res = perimeter(120,110,100)
        self.assertEqual(res, 330)

    def test_area2(self):
        res = area(5.46,10.24)
        self.assertEqual(res, 27.9552)

    def test_perimeter2(self):
        res = perimeter(2.32,41.23,5.14)
        self.assertEqual(res, 48.69)

    def test_area3(self):
        with self.assertRaises(Exception):
            area(-10,-12)

    def test_perimeter3(self):
        with self.assertRaises(Exception):
            perimeter(-5,-4,-123)


if __name__ == "__main__":
    unittest.ma

