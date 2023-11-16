import unittest
def area(a):
    return a * a


def perimeter(a):
    return 4 * a


class SquareTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = area(0)
        self.assertEqual(int(res), 0)

    def test_area_multiple(self):
        res = area(4)
        res1 = area(5)
        res2 = area(10)
        self.assertEqual(int(res), 16)
        self.assertEqual(int(res1), 25)
        self.assertEqual(int(res2), 100)

    def test_perimetr_multiple(self):
        res = perimeter(3)
        res1 = perimeter(4)
        res2 = perimeter(10)
        self.assertEqual(int(res), 12)
        self.assertEqual(int(res1), 16)
        self.assertEqual(int(res2), 40)
    
    def test_perimetr_zero(self):
        res = perimeter(0)
        self.assertEqual(int(res), 0)

