

def area(a, b):
    return a * b
'''
    Принимает 2 числа, которые являются сторонами прямоугольника: a,b
    Возвращает площадь прямоугольника, котоая вычисляется по формуле : a * b
'''
def perimeter(a, b):
    return 2 * (a + b)
'''
    Принимает 2 числа, которые являются сторонами прямоугольника:a,b
    Возвращает периметр треугольника, вычисляя его по формлуе: 2*(a + b)
'''

import unittest
from rectangle import area, perimeter

class RectangleTestCase(unittest.TestCase):
    def test_area_two_and_two(self):
        res = area(2, 2)
        self.assertEqual(res, 4)

    def test_area_two_and_seven(self):
        res = area(2, 7)
        self.assertEqual(res, 14)

    def test_perimeter_one_and_three(self):
        res = perimeter(1, 3)
        self.assertEqual(res, 8)

    def test_perimeter_three_and_five(self):
        res = perimeter(3, 5)
        self.assertEqual(res, 16)

if __name__ == '__main__':
    unittest.main()
