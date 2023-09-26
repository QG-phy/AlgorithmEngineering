import unittest
from dplc.motto.motto import verifyMottoYannanYuan



class TestVerifyMottoYannanYuan(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        pass
    
    def test_verifyMottoYannanYuan_right(self):
        right_motto = "我是最帅的"
        self.assertEqual(verifyMottoYannanYuan(right_motto), True)
        
    def test_verifyMottoYannanYuan_wrong(self):
        wrong_motto = "我不是最帅的"
        self.assertEqual(verifyMottoYannanYuan(wrong_motto), False)
    
    @classmethod
    def tearDownClass(cls):
        pass


if __name__ == '__main__':
    unittest.main()
