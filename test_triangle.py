import unittest
from triangle import area as triangle_area, perimeter as triangle_perimeter

class TestTriangle(unittest.TestCase):
	def test_a_zero_area(self):
		self.assertEqual(triangle_area(0, 25), 0)

	def test_h_zero_area(self):
		self.assertEqual(triangle_area(25, 0), 0)

	def test_small_area(self):
		self.assertEqual(triangle_area(1, 1), 0.5)

	def test_large_area(self):
		self.assertEqual(triangle_area(312564, 23425), 3660905850)

	def test_small_perimeter(self):
		self.assertEqual(triangle_perimeter(1, 1, 1), 3)

	def test_large_perimeter(self):
		self.assertEqual(triangle_perimeter(324234, 234235, 235235), 793704)

	def test_negative_numbers_area(self):
		with self.assertRaises(ValueError):
			triangle_area(-10, 15)
		with self.assertRaises(ValueError):
			triangle_area(10, -15)
		with self.assertRaises(ValueError):
			triangle_area(-10, -15)

	def test_negative_numbers_perimeter(self):
		with self.assertRaises(ValueError):
			triangle_perimeter(-1, 1, 1)
		with self.assertRaises(ValueError):
			triangle_perimeter(-1, -1, 1)
		with self.assertRaises(ValueError):
			triangle_perimeter(-1, -1, -1)

	def test_types(self):
		with self.assertRaises(TypeError):
			triangle_area([1,1])
		with self.assertRaises(TypeError):
			triangle_area({1:1, 2:1})
		with self.assertRaises(TypeError):
			triangle_area("1 1")
		with self.assertRaises(TypeError):
			triangle_perimeter([1,1,1])
		with self.assertRaises(TypeError):
			triangle_perimeter({1:1, 2:1, 3:1})
		with self.assertRaises(TypeError):
			triangle_perimeter("1 1 1")

	def test_is_triangle(self):
		with self.assertRaises(ValueError):
			triangle_perimeter(30, 1, 6)

if __name__ == '__main__':
  unittest.main()
