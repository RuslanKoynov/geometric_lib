import unittest

def area(a, b):
    return a * b

def perimetr(a, b):
    return (a + b) * 2


class RectangleTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = area(0, 0)
        self.assertEqual(res, 0)

    def test_area_multiple(self):
        res = area(4, 5)
        res1 = area(2, 3)
        res2 = area(1, 2)
        self.assertEqual(res, 20)
        self.assertEqual(res1, 6)
        self.assertEqual(res2, 2)

    def test_area_square_value(self):
        res = area(10.52, 10)
        res1 = area(5, 5)
        res2 = area(3, 3)
        self.assertAlmostEqual(res, 105.2, places=1)
        self.assertEqual(res1, 25)
        self.assertEqual(res2, 9)

    def test_perimetr_zero(self):
        res = perimetr(0, 0)
        self.assertEqual(res, 0)

    def test_perimetr_multiple(self):
        res = perimetr(10.52, 2)
        res1 = perimetr(4, 5)
        res2 = perimetr(1, 1)
        self.assertAlmostEqual(res, 25.04, places=2)
        self.assertEqual(res1, 18)
        self.assertEqual(res2, 4)