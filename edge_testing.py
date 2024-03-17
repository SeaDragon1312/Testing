import unittest
from problem_w3 import check_uet_success

"""
    Để chạy test, mở terminal và nhập lệnh edge_testing.py

"""

class CheckUETSuccessEdgeTesting(unittest.TestCase):
    def test_min1(self):
        score = -1
        specialized = "CNTT"
        with self.assertRaises(ValueError):
            check_uet_success(score, specialized)

    def test_min2(self):
        score = 0
        specialized = "CNTT"
        result = check_uet_success(score, specialized)
        self.assertEqual(result, "Trượt")

    def test_min3(self):
        score = 1
        specialized = "CNTT"
        result = check_uet_success(score, specialized)
        self.assertEqual(result, "Trượt")

    def test_max1(self):
        score = 29
        specialized = "CNTT"
        result = check_uet_success(score, specialized)
        self.assertEqual(result, "Đỗ")

    def test_max2(self):
        score = 30
        specialized = "CNTT"
        result = check_uet_success(score, specialized)
        self.assertEqual(result, "Đỗ")

    def test_max3(self):
        score = 31
        specialized = "CNTT"
        with self.assertRaises(ValueError):
            check_uet_success(score, specialized)

    def test_invalid_specialized(self):
        score = 20
        specialized = "Khoa học máy tính"
        with self.assertRaises(ValueError):
            check_uet_success(score, specialized)

if __name__ == '__main__': 
    suite = unittest.TestLoader().loadTestsFromTestCase(CheckUETSuccessEdgeTesting)
    unittest.TextTestRunner(verbosity=2).run(suite)