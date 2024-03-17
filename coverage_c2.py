import unittest
from problem_w3 import check_uet_success
"""
    Để chạy test, mở terminal và nhập lệnh python coverage_c2.py

"""
class CheckUETSuccessCoverageC2(unittest.TestCase):
    def test1(self):
        score = -10
        specialized = "CNTT"
        with self.assertRaises(ValueError):
            check_uet_success(score, specialized)

    def test2(self):
        score = 25
        specialized = "Other"
        with self.assertRaises(ValueError):
            check_uet_success(score, specialized)

    def test3(self):
        score = 25
        specialized = "CKT"
        result = check_uet_success(score, specialized)
        self.assertEqual(result, "Đỗ")

    def test4(self):
        score = 29
        specialized = "CNTT"
        result = check_uet_success(score, specialized)
        self.assertEqual(result, "Đỗ")

    def test5(self):
        score = 20
        specialized = "CNTT"
        result = check_uet_success(score, specialized)
        self.assertEqual(result, "Trượt")

if __name__ == '__main__': 
    suite = unittest.TestLoader().loadTestsFromTestCase(CheckUETSuccessCoverageC2)
    unittest.TextTestRunner(verbosity=2).run(suite)