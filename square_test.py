import unittest
def area(a):
    return a * a
    '''
    Принимает число, которое является стороной квадрата
    Возвращает площадь квадрата, которое вычисляется по формуле: а^2
    '''
def perimeter(a):
    return 4 * a
    '''
    Принимает число, которое является стороной квадрата
    Возвращает периметр квадрата, выячисляя его по формуле : P=4*a
    '''
class SquareTestCase (unittest.TestCase):
    def test_area_two(self):
        res = area(2)
        self.assertEqual(res, 4)

    def test_area_six(self):
        res = area(6)
        self.assertEqual(res,  36)
    def test_perimetr_two(self):
        res = perimeter (2)
        self.assertEqual(res,  8)
    def test_perimetr_fifteen (self):
        res = perimeter (15)
        self.assertEqual (res, 60)

if __name__ == '__main__':
    unittest.main()