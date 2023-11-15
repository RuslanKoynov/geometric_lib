import unittest
import pryamoyg

class PryamoygTestCase (unittest.TestCase):
    def test_pryamoyg_area_1(self):
        self.assertEqual(pryamoyg.area(4,5),20)

    def test_pryamoyg_area_2(self):
        self.assertEqual(pryamoyg.area(5, 6), 30)

    def test_pryamoyg_area_3(self):
        self.assertEqual(pryamoyg.area(6,7),42)



    def test_pryamoyg_perimeter_1(self):
        self.assertEqual(pryamoyg.perimeter(4, 5), 18)

    def test_pryamoyg_perimeter_2(self):
        self.assertEqual(pryamoyg.perimeter(5, 6), 22)

    def test_pryamoyg_perimeter_3(self):
        self.assertEqual(pryamoyg.perimeter(6, 7), 26)


if __name__ == '__main__':
    unittest.main()