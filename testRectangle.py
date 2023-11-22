from rectangle import perimetr, area

class RectangleTest(unittest.TestCase):

    def test_area_Rectangle_Five_Three(self):
        res = area(5, 3)
        self.assertEqual(res, 15)

    def test_area_Circle_Seven_Four(self):
        res = area(7,4)
        self.assertEqual(res, 28)

    def test_area_Circle_Nine_Two(self):
        res = area(9,2)
        self.assertEqual(res, 18)

    def test_perimeter_Rectangle_Five_Two(self):
        res = perimeter(5,2)
        self.assertEqual(res, 14)

    def test_perimeter_Rectangle_MinusSeven_Five(self):
        res = perimeter(-7,5)
        self.assertEqual(res, "ERROR")

    def test_perimeter_Rectangle_Nine_Three(self):
        res = perimeter(9,3)
        self.assertEqual(res, 24)