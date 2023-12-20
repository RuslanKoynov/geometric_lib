import unittest
def area(a, b):
    '''
    Возвращает площадь прямоугольника

      Параметры:
           a (int):значение одной стороны прямоугольника
           b (int):значение второй стороны прямоугольника
    ''' 
    return a * b 

def perimeter(a, b): 
    '''
    Возвращает периметр прямоугольника

      Параметры:
            a (int):значение одной стороны прямоугольника
           b (int):значение второй стороны прямоугольника
    '''
    return 2*(a + b)

class RectangleTest(unittest.TestCase):

    def test_area1(self):
        res = area(1,2)
        self.assertEqual(res, 2)

    def test_perimeter1(self):
        res = perimeter(5,5)
        self.assertEqual(res, 20)

    def test_area2(self):
        res = area(4.5,6.5)
        self.assertEqual(res, 29.25)

    def test_perimeter2(self):
        res = perimeter(4.5,6.5)
        self.assertEqual(res, 22)

    def test_area3(self):
        with self.assertRaises(Exception):
            area(-10,-5)

    def test_perimeter3(self):
        with self.assertRaises(Exception):
            perimeter(-5,-10)


if __name__ == "__main__":
    unittest.ma

