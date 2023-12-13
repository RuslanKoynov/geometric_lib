import unittest
from rectangle import area as rectangle_area, perimeter as rectangle_perimeter

class TestRectangle(unittest.TestCase):
	def test_a_zero_area(self):
		self.assertEqual(rectangle_area(0, 25), 0)

	def test_b_zero_area(self):
		self.assertEqual(rectangle_area(25, 0), 0)

	def test_small_area(self):
		self.assertEqual(rectangle_area(1, 1), 1)

	def test_large_area(self):
		self.assertEqual(rectangle_area(2352, 324266), 762673632)

	def test_a_zero_perimeter(self):
		self.assertEqual(rectangle_perimeter(0, 25), 50)

	def test_b_zero_perimeter(self):
		self.assertEqual(rectangle_perimeter(25, 0), 50)

	def test_small_perimeter(self):
		self.assertEqual(rectangle_perimeter(1, 1), 4)

	def test_large_perimeter(self):
		self.assertEqual(rectangle_perimeter(14241, 5355), 39192)

	def test_negative_numbers_area(self):
		with self.assertRaises(ValueError):
			rectangle_area(-1, 1)
		with self.assertRaises(ValueError):
			rectangle_area(1, -1)
		with self.assertRaises(ValueError):
			rectangle_area(-1, -1)

	def test_negative_numbers_perimeter(self):
		with self.assertRaises(ValueError):
			rectangle_perimeter(-1, 1)
		with self.assertRaises(ValueError):
			rectangle_perimeter(1, -1)
		with self.assertRaises(ValueError):
			rectangle_perimeter(-1, -1)

	def test_types(self):
		with self.assertRaises(TypeError):
			rectangle_area([1,1])
		with self.assertRaises(TypeError):
			rectangle_area({1:1, 2:1})
		with self.assertRaises(TypeError):
			rectangle_area("1 1")
		with self.assertRaises(TypeError):
			rectangle_perimeter([1,1])
		with self.assertRaises(TypeError):
			rectangle_perimeter({1:1, 2:1})
		with self.assertRaises(TypeError):
			rectangle_perimeter("1 1")

if __name__ == '__main__':
  unittest.main()
