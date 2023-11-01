class TriangleTestCase(unittest.TestCase):
   def test_zero_mul(self):
       res = area(10, 0)
       self.assertEqual(res, 0)
       
   def test_square_mul(self):
       res = area(10, 10)
       self.assertEqual(res, 50)

    def test_perimeter(self):
       res = perimeter(10, 5,100)
       self.assertEqual(res, 115)

class CircleTestCase(unittest.TestCase):
   def test_zero_mul(self):
       res = area(0)
       self.assertEqual(res, 0.0)
       
   def test_area(self):
       res = area(10)
       self.assertEqual(res, 314.1592653589793)

    def test_perimeter(self):
       res = perimeter(7)
       self.assertEqual(res, 43.982297150257104)


class SquareTestCase(unittest.TestCase):
   def test_zero_mul(self):
       res = area(0)
       self.assertEqual(res, 0)
       
   def test_area(self):
       res = area(10)
       self.assertEqual(res, 100)

    def test_perimeter(self):
       res = perimeter(7)
       self.assertEqual(res, 28)

if __name__ == "__main__":
  unittest.main()
