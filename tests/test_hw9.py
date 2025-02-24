import unittest
from hw9 import sequence, is_opposite, is_valid

class TestSequence(unittest.TestCase):
    def test_1(self):
        #sequence([1, 2, 3])) -> True
        self.assertEqual(sequence([1, 2, 3]),True)

    def test_2(self):
        #[1, 2, 1, 2] -> False
        self.assertEqual(sequence([1, 2, 1, 2]),False)

class TestIsOpposite(unittest.TestCase):
    def test_1(self):
        self.assertEqual(is_opposite(10,6), 1)

    def test_2(self):
        self.assertEqual(is_opposite(12, 2), 8)
    def test_3(self):
        self.assertEqual(is_opposite(10,2), 7)

class TestIsValid(unittest.TestCase):
    def test_1(self):
        self.assertEqual(is_valid(123), 'Некорректный ввод')
    def test_2(self):
        self.assertEqual(is_valid(4561261212345464), False)
    def test_3(self):
        self.assertEqual(is_valid(4561261212345467), True)
    def test_4(self):
        self.assertEqual(is_valid(378282246310005), True)
    def test_5(self):
        self.assertEqual(is_valid(''), 'Некорректный ввод')
    def test_6(self):
        self.assertEqual(is_valid(56105911231018250), False)
    def test_7(self):
        self.assertEqual(is_valid(6011000990139424), True)
    def test_8(self):
        self.assertEqual(is_valid(5105105105105100), True)