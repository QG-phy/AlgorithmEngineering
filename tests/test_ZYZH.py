import unittest
from dplc.motto.motto import verifyMottoZYZH

class TestVerifyZYZH(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        pass
    
    def test_verifyMottoZYZH_right(self):
        right_motto = "The dice is cast."
        self.assertEqual(verifyMottoZYZH(right_motto), True)
        
    def test_verifyMottoZYZH_wrong(self):
        wrong_motto = "what so ever"
        self.assertEqual(verifyMottoZYZH(wrong_motto), False)
    
    @classmethod
    def tearDownClass(cls):
        pass

if __name__ == '__main__':
    unittest.main()
