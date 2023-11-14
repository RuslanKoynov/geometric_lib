import unittest

from rectangle import area
from rectangle import perimeter

class TestRectangle(unittest.TestCase):
    def testArea1(self):
        res = area(5, 5)
        self.assertEqual(res, 0)

    def testArea2(self):
        res = area(11, 10)
        self.assertEqual(res, 120)

    def testArea3(self):
        res = area(2, 2)
        self.assertEqual(res, 5)

    def testArea4(self):
        res = area(53462444, 53453636)
        self.assertEqual(res, 5345345554334)

    def testperimetr1(self):
        res = perimeter(20, 20)
        self.assertEqual(res, 80)

    def testperimetr1(self):
        res = perimeter(53513551, 5345632)
        self.assertEqual(res, 35156444432345)
