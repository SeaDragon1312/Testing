import unittest
from problem_w3 import check_uet_success

"""
    Để chạy test, trong terminal gõ lệnh python dicision_table.py

"""

class CheckingUETSuccess(unittest.TestCase):
    def test_R1(self):
        specialized = "CNTT"
        score = 20
        result = check_uet_success(score, specialized)
        self.assertEqual(result, "Trượt")
    
    def test_R2(self):
        specialized = "CNTT"
        score = 26
        result = check_uet_success(score, specialized)
        self.assertEqual(result, "Trượt")
    
    def test_R3(self):
        specialized = "CNTT"
        score = 29
        result = check_uet_success(score, specialized)
        self.assertEqual(result, "Đỗ")

    def test_R4(self):
        specialized = "CKT"
        score = 20
        result = check_uet_success(score, specialized)
        self.assertEqual(result, "Trượt")

    def test_R5(self):
        specialized = "CKT"
        score = 26
        result = check_uet_success(score, specialized)
        self.assertEqual(result, "Đỗ")

    def test_R6(self):
        specialized = "CKT"
        score = 29
        result = check_uet_success(score, specialized)
        self.assertEqual(result, "Đỗ")

    def test_invalid_specialized(self):
        specialized = "Khoa học máy tính"
        score = 20
        with self.assertRaises(ValueError):
            check_uet_success(score, specialized)

    def test_invalid_score(self):
        specialized = "CNTT"
        score = 32
        with self.assertRaises(ValueError):
            check_uet_success(score, specialized)

if __name__ == '__main__': 
    suite = unittest.TestLoader().loadTestsFromTestCase(CheckingUETSuccess)
    unittest.TextTestRunner(verbosity=2).run(suite)
