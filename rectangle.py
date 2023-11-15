import unittest

def area(a, b):
    '''
    Принимает два числа, которые являются сторонами прямоугольника: a, b
    Возвращает площадь прямоугольника, вычисляя ее по формуле: a * b
    '''
    return a * b


def perimeter(a, b):
    '''
    Принимает два числа, которые являются сторонами прямоугольника: a, b
    Возвращает периметр прямоугольника, вычисляя его по формуле: 2 * (a + b)
    '''
    return 2 * (a + b)


class RectangleTestCase(unittest.TestCase):
    def test_area_2_and_2(self):
        res = area(2, 2)
        self.assertEqual(res, 4)

    def test_area_3_and_5(self):
        res = area(3, 5)
        self.assertEqual(res, 15)

    def test_perimetr_2_and_2(self):
        res = perimeter(2, 2)
        self.assertEqual(res, 8)

    def test_perimetr_3_and_5(self):
        res = perimeter(3, 5)
        self.assertEqual(res, 16)
