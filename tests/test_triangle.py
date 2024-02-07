import unittest
import triangle
from contextlib import nullcontext as does_not_raise


class TestSquare(unittest.TestCase):
    def test_area(self):
        eps = 0.1 ** 5
        params = [
            (0.001, 2, 0.001, does_not_raise(), ''),
            (2, 0.001, 0.001, does_not_raise(), ''),
            (10, 20, 100, does_not_raise(), ''),
            (0, 10, None, self.assertRaises(ValueError), 'The side and height of a triangle must be greater than zero'),
            (10, 0, None, self.assertRaises(ValueError), 'The side and height of a triangle must be greater than zero'),
            (-1, 10, None, self.assertRaises(ValueError), 'The side and height of a triangle must be greater than zero'),
            (10, -1, None, self.assertRaises(ValueError), 'The side and height of a triangle must be greater than zero'),
            ('ab', 10, None, self.assertRaises(TypeError), 'The side and height of a triangle must be int or float'),
            (10, 'ab', None, self.assertRaises(TypeError), 'The side and height of a triangle must be int or float')
        ]
        for a, h, excepted, exc, exc_message in params:
            with self.subTest():
                with exc as context:
                    res = triangle.area(a, h)
                if context is not None:
                    self.assertEqual(
                        exc_message,
                        str(context.exception)
                    )
                else:
                    self.assertTrue(
                        excepted - eps <= res <= excepted + eps,
                        f'{res}(result) != {excepted}(excepted result)'
                    )

    def test_perimeter(self):
        eps = 0.1 ** 5
        params = [
            (0.001, 0.002, 0.0025, 0.0055, does_not_raise(), ''),
            (10, 20, 25, 55, does_not_raise(), ''),
            (10, 20, 30,  None, self.assertRaises(ValueError), 'The sum of two sides of a triangle must be greater than last side'),
            ('ab', 20, 25, None, self.assertRaises(TypeError), 'All sides of a triangle must be int or float'),
            (10, 'ab', 25, None, self.assertRaises(TypeError), 'All sides of a triangle must be int or float'),
            (10, 20, 'ab', None, self.assertRaises(TypeError), 'All sides of a triangle must be int or float'),
        ]
        for a, b, c, excepted, exc, exc_message in params:
            with self.subTest():
                with exc as context:
                    res = triangle.perimeter(a, b, c)
                if context is not None:
                    self.assertEqual(
                        exc_message,
                        str(context.exception)
                    )
                else:
                    self.assertTrue(
                        excepted - eps <= res <= excepted + eps,
                        f'{res}(result) != {excepted}(excepted result)'
                    )
