import unittest
import square


class SquareTestCase(unittest.TestCase):
    def test_zero_area(self):
        with self.assertRaises(ValueError):
            res = square.area(0)

        def test_positive_area(self):
            res = square.area(100)
            self.assertEqual(res, 1000)

        def test_negative_side_square_area(self):
            res = area(-4)
            with self.assertRaises(ValueError):
                res = square.area(0)

        def test_zero_perimeter(self):
            with self.assertRaises(ValueError):
                res = square.perimetr(0)

            def test_positive_perimeter(self):
                res = square.perimeter(100)
                self.assertEqual(res, 400)

            def test_negative_side_square_perimetr(self):
                with self.assertRaises(ValueError):
                    res = square.perimetr(0)
