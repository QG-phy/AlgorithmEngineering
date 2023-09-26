import unittest
from dplc.motto.motto import verifyMottoYiboWang



class TestVerifyMottoYiboWang(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        pass
    
    def test_verifyMottoYiboWang_right(self):
        right_motto = "i love china"
        self.assertEqual(verifyMottoYiboWang(right_motto), True)
        
    def test_verifyMottoYiboWang_wrong(self):
        wrong_motto = "湖人总冠军"
        self.assertEqual(verifyMottoYiboWang(wrong_motto), False)
    
    @classmethod
    def tearDownClass(cls):
        pass


if __name__ == '__main__':
    unittest.main()
