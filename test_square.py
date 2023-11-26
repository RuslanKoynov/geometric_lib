import unittest

from square import area
from square import perimeter

class TestSquare(unittest.TestCase):
    def test_Area1(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_Area2(self):
        res = area(1)
        self.assertEqual(res, 1)

    def test_Area3(self):
        res = area(534534)
        self.assertEqual(res, 285726597156)

    def test_Perimeter1(self):
        res = perimeter(10)
        self.assertEqual(res, 40)

    def test_Perimeter(self):
        res = perimeter(62423423)
        self.assertEqual(res, 249693692)

if __name__ == '__main__':
    unittest.main()