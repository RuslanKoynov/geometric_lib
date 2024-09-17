import unittest
from figures.circle import area as circle_area, perimeter as circle_perimeter
from figures.rectangle import area as rec_area, perimeter as rec_perimeter
from figures.square import area as square_area, perimeter as square_perimeter
from figures.triangle import area as triangle_area, perimeter as triangle_perimeter

class TestCircle(unittest.TestCase):

    def test_circle_area(self):
        self.assertEqual(circle_area(5), 78.54)

    def test_circle_perimeter(self):
        self.assertEqual(circle_perimeter(5), 31.42)


class TestRectangle(unittest.TestCase):

    def test_rec_area(self):
        self.assertEqual(rec_area(5, 7), 35)

    def test_rec_perimeter(self):
        self.assertEqual(rec_perimeter(5, 15), 40)


class TestSquare(unittest.TestCase):

    def test_square_area(self):
        self.assertEqual(square_area(5), 25)

    def test_square_perimeter(self):
        self.assertEqual(square_perimeter(5), 20)


class TestTriangle(unittest.TestCase):

    def test_triangle_area(self):
        self.assertEqual(triangle_area(3, 5), 7.5)

    def test_triangle_perimeter(self):
        self.assertEqual(triangle_perimeter(5, 10, 15), 30)


if __name__ == '__main__':
    unittest.main()

