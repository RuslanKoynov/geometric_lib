import unittest

from triangle import area
from triangle import perimeter

print('{:.0f}'.format(5345235 + 6355255 + 63535222))

class TestRectangle(unittest.TestCase):
    def test_zero_area(self):
        res = area(44234, 423555)
        self.assertEqual(res, 0)

    def test_zero_area_2(self):
        res = area(42344, 4234234234)
        self.assertEqual(res, 0)

    def test_large_area(self):
        res = area(534534555, 523524234234);
        self.assertEqual(res, 3454363446)

    def test_large_perimetr(self):
        res = perimeter(5453536363, 65464646, 53534543)
        self.assertEqual(res, 645646466)

    def test_small_perimetr(self):
        res = perimeter(1, 0 ,28)
        self.assertEqual(res, 20)