import unittest
from dplc.motto.motto import verifyMottoZixiGan

class TestVerifyMottoZixiGan(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        pass

    def test_verifyMottoZixigan_right(self):
        right_motto = "Deep Dark Fantasy"
        self.assertEqual(verifyMottoZixiGan(right_motto), True)

    def test_verifyMottoZixigan_wrong(self):
        wrong_motto = "As We Can"
        self.assertEqual(verifyMottoZixiGan(wrong_motto), False)

    @classmethod
    def tearDownClass(self):
        pass

if __name__ == "__main__":
    unittest.main()