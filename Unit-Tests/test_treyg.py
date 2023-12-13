import unittest
import treyg

class TreygTestCase(unittest.TestCase):
    def test_treyg_area_1(self):
        self.assertEqual(treyg.area(4,1), 2)

    def test_treyg_area_2(self):
        self.assertEqual(treyg.area(5,2), 5)

    def test_treyg_area_3(self):
        self.assertEqual(treyg.area(6,3), 9)



    def test_treyg_perimeter_1(self):
        self.assertEqual(treyg.perimeter(2,2,3), 7)

    def test_treyg_perimeter_2(self):
        self.assertEqual(treyg.perimeter(3,3,4), 10)

    def test_treyg_perimeter_3(self):
        self.assertEqual(treyg.perimeter(4,4,5), 13)


if __name__ == '__main__':
    unittest.main()