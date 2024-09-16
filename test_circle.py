import unittest
import circle


class CircleTest(unittest.TestCase):
    """Набор unit test, который проверяет правильность работы функции для вычисления площади круга"""
    def test_area_1(self):
        res = circle.area(3)
        self.assertEqual(res, 28.274333882308138)

    def test_area_2(self):
        res = circle.area(0)
        self.assertEqual(res, "The figure doesn't exist")

    def test_area_3(self):
        res = circle.area(-1)
        self.assertEqual(res, 'Invalid input')

    def test_area_4(self):
        res = circle.area('qw')
        self.assertEqual(res, 'Invalid input')

    def test_area_5(self):
        res = circle.area(True)
        self.assertEqual(res, 'Invalid input')

    """Набор unit test, который проверяет правильность работы функции для вычисления длины окружности"""
    def test_perimeter_1(self):
        res = circle.perimeter(3)
        self.assertEqual(res, 18.84955592153876)

    def test_perimeter_2(self):
        res = circle.perimeter(0)
        self.assertEqual(res, "The figure doesn't exist")

    def test_perimeter_3(self):
        res = circle.perimeter(-1)
        self.assertEqual(res, 'Invalid input')

    def test_perimeter_4(self):
        res = circle.perimeter('qw')
        self.assertEqual(res, 'Invalid input')

    def test_perimeter_5(self):
        res = circle.perimeter(True)
        self.assertEqual(res, 'Invalid input')


if __name__ == '__main__':
    unittest.main()
