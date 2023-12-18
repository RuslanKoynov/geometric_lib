import unittest
import square

class SquareTestCase(unittest.TestCase):
    def test_square_area_1(self):
        self.assertEqual(square.area(4), 16)

    def test_square_area_2(self):
        self.assertEqual(square.area(5), 25)

    def test_square_area_3(self):
        self.assertEqual(square.area(6), 36)



    def test_square_area_1(self):
        self.assertEqual(square.perimeter(4), 16)

    def test_square_area_3(self):
        self.assertEqual(square.perimeter(5), 20)

    def test_square_area_3(self):
        self.assertEqual(square.perimeter(6), 24)


if __name__ == '__main__':
    unittest.main()