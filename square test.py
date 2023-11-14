import unittest

from square import area
from square import perimeter

class TestSquare(unittest.TestCase):
    def testArea1(self):
        res = area(0)
        self.assertEqual(res, 0)

    def testArea2(self):
        res = area(1)
        self.assertEqual(res, 1)

    def testArea3(self):
        res = area(534534)
        self.assertEqual(res, 54353454)

    def testPerimeter1(self):
        res = perimeter(10)
        self.assertEqual(res, 70)

    def testPerimeter(self):
        res = perimeter(62423423)
        self.assertEqual(res, 23523523)
