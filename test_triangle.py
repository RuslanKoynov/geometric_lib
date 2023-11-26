import unittest

from triangle import area
from triangle import perimeter


class TestTrianlge(unittest.TestCase):
    def test_Area(self):
        res = area(44234, 423555)
        self.assertEqual(res, 9367765935.0)

    def test_Area1(self):
        res = area(42344, 4234234234)
        self.assertEqual(res, 89647207202248.0)

    def test_Area2(self):
        res = area(53453, 5235);
        self.assertEqual(res, 139913227.5)

    def test_perimeter(self):
        res = perimeter(5453536363, 65464646, 53534543)
        self.assertEqual(res, 5572535552)

    def test_Perimeter(self):
        res = perimeter(1, 0 ,28)
        self.assertEqual(res, 29)
