import unittest

def SquarityFunction(z):
    '''
    STDIN: the value of the variable
    STDOUT: the value of the variable squared
    '''
    return z**2

class SquarityFunctionTestCase(unittest.TestCase):
    def test_negative_integer(self):
        result = SquarityFunction(-15)
        self.assertEqual(result, 225)

    def test_zero(self):
        result = SquarityFunction(0)
        self.assertEqual(result, 0)
    
    def test_positive_integer(self):
        result = SquarityFunction(5)
        self.assertEqual(result, 25)

    def test_fraction(self):
        result = SquarityFunction(1.5)
        self.assertEqual(result, 2.25)
