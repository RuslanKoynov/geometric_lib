import unittest

def area(a):
    '''
    Возвращает площадь квадрата

        Параметры:
            a (int): сторона квадрата
        Возвращаемое значение:
            сторона в квадрате
    
    '''
    if a < 0:
        raise ValueError("Negative number")
    
    return a * a

def perimeter(a):
    '''
    Возвращает периметр квадрата

        Параметры:
            a (int): сторона квадрата
        Возвращаемое значение:
            сторона, умноженная на 4
    
    '''
    return 4 * a

class SquareTestCase(unittest.TestCase):

    def test_area_positive_side(self):
        res = area(5)
        self.assertEqual(res, 25)

    def test_area_negative_side(self):
        with self.assertRaises(ValueError):
            area(-3)

    def test_perimeter_zero_side(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_mixed_side(self):
        res = perimeter(4)
        self.assertEqual(res, 16)

    def test_area_float_side(self):
        res = area(2.5)
        self.assertAlmostEqual(res, 6.25, places=2)
        
    def test_perimeter_float_side(self):
        res = perimeter(3.5)
        self.assertAlmostEqual(res, 14, places=2)

if __name__ == '__main__':
    unittest.main()
