import unittest
from dplc.motto.motto import verifyMottoZheyuanHu



class TestVerifyMottoZheyuanHu(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        pass
    
    def test_verifyMottoZheyuanHu_right(self):
        right_motto = "Nice to meet you!"
        self.assertEqual(verifyMottoZheyuanHu(right_motto), True)
        
    def test_verifyMottoZheyuanHu_wrong(self):
        wrong_motto = "湖人总冠军"
        self.assertEqual(verifyMottoZheyuanHu(wrong_motto), False)
    
    @classmethod
    def tearDownClass(cls):
        pass


if __name__ == '__main__':
    unittest.main()
