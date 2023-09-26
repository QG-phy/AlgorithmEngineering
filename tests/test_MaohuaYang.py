import unittest
from dplc.motto.motto import verifyMottoMaohuaYang



class TestVerifyMottoMaohuaYang(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        pass
    
    def test_verifyMottoMaohuaYang_right(self):
        right_motto = "boat to bridge head nature"
        self.assertEqual(verifyMottoMaohuaYang(right_motto), True)
        
    def test_verifyMottoMaohuaYang_wrong(self):
        wrong_motto = "湖人总冠军"
        self.assertEqual(verifyMottoMaohuaYang(wrong_motto), False)
    
    @classmethod
    def tearDownClass(cls):
        pass


if __name__ == '__main__':
    unittest.main()
