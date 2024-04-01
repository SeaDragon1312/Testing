import unittest
from problem_w3 import caculate_baking_time
"""
    Để chạy test, mở terminal và nhập lệnh python coverage_c2.py

"""
class CheckCoverangeC2(unittest.TestCase):
    def test1(self):
        mass = 1
        meatName = "Chó"
        with self.assertRaises(ValueError):
            caculate_baking_time(mass, meatName)

    def test2(self):
        mass = 6
        meatName = "Lợn"
        with self.assertRaises(ValueError):
            caculate_baking_time(mass, meatName)

    def test3(self):
        mass = 1
        meatName = "Lợn"
        result = caculate_baking_time(mass, meatName)
        self.assertEqual(result, 10)

    def test4(self):
        mass = 3
        meatName = "Lợn"
        result = caculate_baking_time(mass, meatName)
        self.assertEqual(result, 25)

    def test5(self):
        mass = 1
        meatName = "Gà"
        result = caculate_baking_time(mass, meatName)
        self.assertEqual(result, 8)

    def test6(self):
        mass = 3
        meatName = "Gà"
        result = caculate_baking_time(mass, meatName)
        self.assertEqual(result, 20)

if __name__ == '__main__': 
    suite = unittest.TestLoader().loadTestsFromTestCase(CheckCoverangeC2)
    unittest.TextTestRunner(verbosity=2).run(suite)