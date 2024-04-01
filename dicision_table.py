import unittest
from problem_w3 import caculate_baking_time

"""
    Để chạy test, trong terminal gõ lệnh python dicision_table.py

"""

class CheckingUETSuccess(unittest.TestCase):
    def test_R1(self):
        meatName = "Lợn"
        mass = 1
        result = caculate_baking_time(mass, meatName)
        self.assertEqual(result, 10)
    
    def test_R2(self):
        meatName = "Lợn"
        mass = 3
        result = caculate_baking_time(mass, meatName)
        self.assertEqual(result, 25)
    
    def test_R3(self):
        meatName = "Gà"
        mass = 1
        result = caculate_baking_time(mass, meatName)
        self.assertEqual(result, 8)

    def test_R4(self):
        meatName = "Gà"
        mass = 3
        result = caculate_baking_time(mass, meatName)
        self.assertEqual(result, 20)

    def test_invalid_meatName(self):
        meatName = "Bò"
        mass = 2
        with self.assertRaises(ValueError):
            caculate_baking_time(mass, meatName)

    def test_invalid_mass(self):
        meatName = "Lợn"
        mass = 6
        with self.assertRaises(ValueError):
            caculate_baking_time(mass, meatName)

if __name__ == '__main__': 
    suite = unittest.TestLoader().loadTestsFromTestCase(CheckingUETSuccess)
    unittest.TextTestRunner(verbosity=2).run(suite)
