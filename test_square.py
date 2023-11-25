import unittest
from square import area as square_area, perimeter as square_perimeter

class TestSquare(unittest.TestCase):
	def test_zero_area(self):
		self.assertEqual(square_area(0), 0)

	def test_small_area(self):
		self.assertEqual(square_area(1), 1)

	def test_large_area(self):
		self.assertEqual(square_area(1244), 1547536)

	def test_zero_perimeter(self):
		self.assertEqual(square_perimeter(0), 0)

	def test_small_perimeter(self):
		self.assertEqual(square_perimeter(1), 4)

	def test_large_perimeter(self):
		self.assertEqual(square_perimeter(3223), 12892)

	def test_negative_numbers_area(self):
		with self.assertRaises(ValueError):
			square_area(-1)

	def test_negative_numbers_perimeter(self):
		with self.assertRaises(ValueError):
			square_perimeter(-1)

	def test_types(self):
		with self.assertRaises(TypeError):
			square_area([1])
		with self.assertRaises(TypeError):
			square_area({1:1})
		with self.assertRaises(TypeError):
			square_area("1")
		with self.assertRaises(TypeError):
			square_perimeter([1])
		with self.assertRaises(TypeError):
			square_perimeter({1:1})
		with self.assertRaises(TypeError):
			square_perimeter("1")

if __name__ == '__main__':
  unittest.main()
