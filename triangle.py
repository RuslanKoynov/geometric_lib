import unittest

def area(a, h):
    return a * h / 2

def perimetr(a, b, c):
    return a + b + c

class TriangleTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = area(0, 0)
        self.assertEqual(res, 0)

    def test_area_multiple(self):
        res = area(10.6, 2)
        res1 = area(4, 3)
        res2 = area(11, 3)
        self.assertAlmostEqual(res, 10.6, places=1)
        self.assertAlmostEqual(res1, 6.0, places=1)
        self.assertAlmostEqual(res2, 16.5, places=1)

    def test_perimetr_zero(self):
        res = perimetr(0, 0, 0)
        self.assertEqual(res, 0)

    def test_perimetr_multiple(self):
        res = perimetr(10.5, 2, 3)
        res1 = perimetr(5, 3, 1)
        self.assertEqual(res, 15.5)
        self.assertEqual(res1, 9)