import unittest
from dplc.motto.motto import verifyMottoQiangqiangGu



class TestVerifyMottoQiangqiangGu(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        pass
    
    def test_verifyMottoQiangqiangGu_right(self):
        right_motto = "Hope for the best!"
        self.assertEqual(verifyMottoQiangqiangGu(right_motto), True)
        
    def test_verifyMottoQiangqiangGu_wrong(self):
        wrong_motto = "a wrong motto"
        self.assertEqual(verifyMottoQiangqiangGu(wrong_motto), False)
    
    @classmethod
    def tearDownClass(cls):
        pass


if __name__ == '__main__':
    unittest.main()
