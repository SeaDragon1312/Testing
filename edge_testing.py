import unittest
from problem_w3 import caculate_baking_time

"""
    Để chạy test, mở terminal và nhập lệnh python edge_testing.py

"""

class CheckCaculateEdgeTesting(unittest.TestCase):
    def test_min1(self):
        mass = 0
        meatName = "Lợn"
        with self.assertRaises(ValueError):
            caculate_baking_time(mass, meatName)

    def test_min2(self):
        mass = 0.1
        meatName = "Lợn"
        result = caculate_baking_time(mass, meatName)
        self.assertEqual(result, 1)

    def test_min3(self):
        mass = 1
        meatName = "Lợn"
        result = caculate_baking_time(mass, meatName)
        self.assertEqual(result, 10)

    def test_max1(self):
        mass = 4
        meatName = "Gà"
        result = caculate_baking_time(mass, meatName)
        self.assertEqual(result, 24)

    def test_max2(self):
        mass = 5
        meatName = "Gà"
        result = caculate_baking_time(mass, meatName)
        self.assertEqual(result, 28)

    def test_max3(self):
        mass = 6
        meatName = "Gà"
        with self.assertRaises(ValueError):
            caculate_baking_time(mass, meatName)

    def test_invalid_meatName(self):
        mass = 2.5
        meatName = "Bò"
        with self.assertRaises(ValueError):
            caculate_baking_time(mass, meatName)

if __name__ == '__main__': 
    suite = unittest.TestLoader().loadTestsFromTestCase(CheckCaculateEdgeTesting)
    unittest.TextTestRunner(verbosity=2).run(suite)