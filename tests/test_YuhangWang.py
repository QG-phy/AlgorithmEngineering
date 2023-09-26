import unittest
from dplc.motto.motto import verifyMottoYuhangWang


class TestVerifyMottoYuhangWang(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        pass

    def test_verifyMottoYuhangWang_right(self):
        right_motto = "介然用之而成路"
        self.assertEqual(verifyMottoYuhangWang(right_motto), True)

    def test_verifyMottoYuhangWang_wrong(self):
        wrong_motto = "面好吃"
        self.assertEqual(verifyMottoYuhangWang(wrong_motto), False)

    @classmethod
    def tearDownClass(cls):
        pass


if __name__ == '__main__':
    unittest.main()
