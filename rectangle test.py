import unittest

from rectangle import area
from rectangle import perimeter

class TestRectangle(unittest.TestCase):
    def testArea1(self):
        res = area(5, 5)
        self.assertEqual(res, 25)

    def testArea2(self):
        res = area(11, 10)
        self.assertEqual(res, 110)

    def testArea3(self):
        res = area(2, 2)
        self.assertEqual(res, 4)

    def testArea4(self):
        res = area(5346, 5345)
        self.assertEqual(res, 28574370)

    def testperimetr1(self):
        res = perimeter(20, 30)
        self.assertEqual(res, 100)

    def testperimetr1(self):
        res = perimeter(5351, 534)
        self.assertEqual(res, 11770)
