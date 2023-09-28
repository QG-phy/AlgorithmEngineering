import unittest
from dplc.motto.motto import verifyMottoJijieZou


class TestVerifyMottoJijieZou(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        pass
    
    def test_verifyMottoJijieZou_right(self):
        right_motto = "You know who"
        self.assertEqual(verifyMottoJijieZou(right_motto), True)
        
    def test_verifyMottoJijieZou_wrong(self):
        wrong_motto = "你猜"
        self.assertEqual(verifyMottoJijieZou(wrong_motto), False)
    
    @classmethod
    def tearDownClass(cls):
        pass


if __name__ == '__main__':
    unittest.main()
