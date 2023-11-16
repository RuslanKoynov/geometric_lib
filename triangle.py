import unittest

def area(a, h):
    return a * h / 2

def perimetr(a, b, c):
    return a + b + c

class TriangleTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = area(0, 0)
        self.assertEqual(int(res), 0)

    def test_area_multiple(self):
        res = area(10, 2)
        res1 = area(4, 3)
        res2 = area(11, 3)
        self.assertEqual(int(res), 10)
        self.assertEqual(int(res1), 6)
        self.assertEqual(int(res2), 16)

    def test_perimetr_zero(self):
        res = perimetr(0, 0, 0)
        self.assertEqual(int(res), 0)

    def test_perimetr_multiple(self):
        res = perimetr(10, 2, 3)
        res1 = perimetr(5, 3, 1)
        self.assertEqual(int(res), 15)
        self.assertEqual(int(res1), 9)