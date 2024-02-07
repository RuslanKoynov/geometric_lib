import unittest
import square
from contextlib import nullcontext as does_not_raise


class TestSquare(unittest.TestCase):
    def test_area(self):
        eps = 0.1 ** 10
        params = [
            (0.001, 0.000001, does_not_raise(), ''),
            (1234, 1522756, does_not_raise(), ''),
            (0, None, self.assertRaises(ValueError), 'The side(a = 0) of a square must be greater than zero'),
            (-1, None, self.assertRaises(ValueError), 'The side(a = -1) of a square must be greater than zero'),
            ('ab', None, self.assertRaises(TypeError), 'The side of a square must be int or float')
        ]
        for a, excepted, exc, exc_message in params:
            with self.subTest():
                with exc as context:
                    res = square.area(a)
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
        eps = 0.1 ** 10
        params = [
            (0.001, 0.004, does_not_raise(), ''),
            (1234, 4936, does_not_raise(), ''),
            (0, None, self.assertRaises(ValueError), 'The side(a = 0) of a square must be greater than zero'),
            (-1, None, self.assertRaises(ValueError), 'The side(a = -1) of a square must be greater than zero'),
            ('ab', None, self.assertRaises(TypeError), 'The side of a square must be int or float')
        ]
        for a, excepted, exc, exc_message in params:
            with self.subTest():
                with exc as context:
                    res = square.perimeter(a)
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
