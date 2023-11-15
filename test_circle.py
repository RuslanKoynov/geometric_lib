import unittest
import circle
import math
class CircleTestCase (unittest.TestCase):
    def test_circle_area_1(self):
        self.assertAlmostEqual(circle.area(3),math.pi * 3 * 3)

    def test_circle_area_2(self):
        self.assertAlmostEqual(circle.area(4),math.pi * 4 * 4)

    def test_circle_area_3(self):
        self.assertAlmostEqual(circle.area(5),math.pi * 5 * 5)



    def test_circle_perimeter_1(self):
        self.assertAlmostEqual(circle.perimeter(3),2 * math.pi * 3)

    def test_circle_perimeter_2(self):
        self.assertAlmostEqual(circle.perimeter(4),2 * math.pi * 4)

    def test_circle_perimeter_3(self):
        self.assertAlmostEqual(circle.perimeter(5),2 * math.pi * 5)


if __name__ == '__main__':
    unittest.main()