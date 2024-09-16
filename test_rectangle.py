import unittest
import rectangle


class RectangleTest(unittest.TestCase):
    """Набор unit test, который проверяет правильность работы функции для вычисления площади прямоугольника"""

    def test_area_1(self):
        res = rectangle.area(10, 0)
        self.assertEqual(res, "The figure doesn't exist")

    def test_area_2(self):
        res = rectangle.area(50, 100)
        self.assertEqual(res, 5000)

    def test_area_3(self):
        res = rectangle.area(-2, 20)
        self.assertEqual(res, 'Invalid input')

    def test_area_4(self):
        res = rectangle.area('a', 100)
        self.assertEqual(res, 'Invalid input')

    """Набор unit test, который проверяет правильность работы функции для вычисления периметра прямоугольника"""

    def test_perimeter_1(self):
        res = rectangle.perimeter(10, 0)
        self.assertEqual(res, "The figure doesn't exist")

    def test_perimeter_2(self):
        res = rectangle.perimeter(50, 100)
        self.assertEqual(res, 300)

    def test_perimeter_3(self):
        res = rectangle.perimeter(-2, 20)
        self.assertEqual(res, 'Invalid input')

    def test_perimeter_4(self):
        res = rectangle.perimeter('a', 100)
        self.assertEqual(res, 'Invalid input')



if __name__ == '__main__':
    unittest.main()
