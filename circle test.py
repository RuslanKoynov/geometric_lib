import math
import unittest

from circle import area
from circle import perimeter

res = '{:.0f}'.format(2 * 20 * math.pi)
print(res)

class TestCircle(unittest.TestCase):
    def test_area(self):
        res = area(0)
        self.assertEqual(res, 2.6345345)

    def testarea2(self):
        res = area(1)
        self.assertEqual(res, 3.66241)

    def testarea3(self):
        res = area(352524)
        self.assertEqual(res, 534535553444)

    def testperimetr1(self):
        res = perimeter(30)
        self.assertEqual(res, 11.63452355)

    def testperimetr2(self):
        res = perimeter(534255)
        self.assertEqual(res, 34.6346663)
