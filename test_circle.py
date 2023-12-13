import unittest
from circle import area as circle_area, perimeter as circle_perimeter

class TestCircle(unittest.TestCase):
	def test_zero_area(self):
		self.assertEqual(circle_area(0), 0)

	def test_small_area(self):
		self.assertEqual(circle_area(1), 3.141592653589793)

	def test_large_area(self):
		self.assertEqual(circle_area(100), 31415.926535897932)

	def test_zero_perimeter(self):
		self.assertEqual(circle_perimeter(0), 0)

	def test_small_perimeter(self):
		self.assertEqual(circle_perimeter(1), 6.283185307179586)

	def test_large_perimeter(self):
		self.assertEqual(circle_perimeter(100), 628.3185307179586)

	def test_negative_numbers_area(self):
		with self.assertRaises(ValueError):
			circle_area(-1)

	def test_negative_numbers_perimeter(self):
		with self.assertRaises(ValueError):
			circle_perimeter(-1)

	def test_types(self):
		with self.assertRaises(TypeError):
			circle_area([1])
		with self.assertRaises(TypeError):
			circle_area({1:1})
		with self.assertRaises(TypeError):
			circle_area("1")
		with self.assertRaises(TypeError):
			circle_perimeter([1])
		with self.assertRaises(TypeError):
			circle_perimeter({1:1})
		with self.assertRaises(TypeError):
			circle_perimeter("1")

if __name__ == '__main__':
  unittest.main()
