import unittest
from triangle import primlenakr
from triangle import sortirovka
from triangle import maxChislo

class Test(unittest.TestCase):
    def test_obchisla(self):
        res = primlenakr(10,1,2)
        self.assertEqual(res,200)
    def test_nyli(self):
        res = primlenakr(0,1,1422)
        self.assertEqual(res,0)
    def test_nylirev(self):
        res = primlenakr(0,0,1422)
        self.assertEqual(res,0)
    def test_nylirev1(self):
        res = primlenakr(0,0,0)
        self.assertEqual(res,0)
    def test_revnyli(self):
        res = primlenakr(0,1,0)
        self.assertEqual(res,0)
    def test_sort(self):
        a = [1,2,3,1,1,1,3]
        self.assertEqual(sortirovka(a),[1,1,1,1,2,3,3])
    def test_revsort(self):
        a = [-1, -2, -3, 1, 1, 1, -3]
        self.assertEqual(sortirovka(a), [-3,-3,-2,-1,1,1,1])
    def test_max(self):
        a = [1,3,3,1,312,231,321,3123,4,-141]
        self.assertEqual(maxChislo(a),3123)

