import unittest

from square import area
from square import perimeter

class TestSquare(unittest.TestCase):
    def test1_square_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test2_square_area(self):
        res = area(1)
        self.assertEqual(res, 1)

    def test3_square_area(self):
        res = area(5)
        self.assertEqual(res, 25)

    def test4_square_area(self):
        res = area(8)
        self.assertEqual(res, 64)

    def test5_square_area(self):
        res = area(12232456)
        self.assertEqual(res, 149632979791936)

    def test6_square_area(self):
        res = area(-12)
        self.assertRaises(res, Exception)

    def test7_square_area(self):
        res = area(7.124124)
        self.assertEqual(res, 50.753142767376005)



    def test1_square_perimetr(self):
        res = perimeter(1)
        self.assertEqual(res, 4)

    def test2_square_perimetr(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test3_square_perimetr(self):
        res = perimeter(12)
        self.assertEqual(res, 48)

    def test4_square_perimetr(self):
        res = perimeter(123456)
        self.assertEqual(res, 493824)

    def test5_square_perimetr(self):
        res = perimeter(-123)
        self.assertRaises(res, Exception)

    def test6_square_perimetr(self):
        res = perimeter(4.3245)
        self.assertEqual(res, 17.298)