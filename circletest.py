import unittest
from circle import area
from circle import perimeter
from math import pi

class CircleTestCase(unittest.TestCase):
    def test_int(self):
        self.assertEqual(area(1),pi*1*1)
        self.assertEqual(area(60),pi*60*60)
        self.assertEqual(perimeter(10),2*pi*10)
        self.assertEqual(perimeter(76),2*pi*76)
    
    def test_float(self):
        self.assertEqual(area(1.5),pi*1.5*1.5)
        self.assertEqual(area(17.7),pi*17.7*17.7)
        self.assertEqual(perimeter(3.5),2*pi*3.5)
        self.assertEqual(perimeter(87.6),2*pi*87.6)
    
    def test_anoter(self):
        self.assertEqual(area(-5),"Радиус не может быть отрицательным")
        self.assertEqual(area("&"),"Радиус должен быть числом, а не символом")
        self.assertEqual(perimeter(-89),"Радиус не может быть отрицательным")
        self.assertEqual(perimeter(";"),"Радиус должен быть числом, а не символом")