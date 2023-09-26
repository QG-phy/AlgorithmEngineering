import unittest
from dplc.motto.motto import verifyMottoYuzhiZhang



class TestVerifyMottoYuzhiZhang(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        pass
    
    def test_verifyMottoYuzhiZhang_right(self):
        right_motto = "Only Paranoia Survive"
        self.assertEqual(verifyMottoYuzhiZhang(right_motto), True)
        
    def test_verifyMottoYuzhiZhang_wrong(self):
        wrong_motto = "湖人总冠军"
        self.assertEqual(verifyMottoYuzhiZhang(wrong_motto), False)
    
    @classmethod
    def tearDownClass(cls):
        pass


if __name__ == '__main__':
    unittest.main()
