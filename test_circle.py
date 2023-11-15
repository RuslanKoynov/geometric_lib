import unittest
import circle

class CircleTestCase (unittest.TestCase):
    def test_circle_area_1(self):
        self.assertEqual(circle.area(3),28.274,places=3)

    def test_circle_area_2(self):
        self.assertEqual(circle.area(4),50.265,places=3)

    def test_circle_area_3(self):
        self.assertEqual(circle.area(5),78.539,places=3)



    def test_circle_perimeter_1(self):
        self.assertEqual(circle.perimeter(3),18.849,places=3)

    def test_circle_perimeter_2(self):
        self.assertEqual(circle.perimeter(4),25.132,places=3)

    def test_circle_perimeter_3(self):
        self.assertEqual(circle.perimeter(5),31.415,places=3)


if __name__ == '__main__':
    unittest.main()