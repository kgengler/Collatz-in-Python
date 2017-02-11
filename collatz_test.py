import unittest
from collatz import collatz

class CollatzTest(unittest.TestCase):
    def test_collatz_1(self):
        self.assertEqual(collatz(1), 0)

    def test_collatz_2(self):
        self.assertEqual(collatz(2), 1)

    def test_collatz_9(self):
        self.assertEqual(collatz(9), 19)

    def test_collatz_27(self):
        self.assertEqual(collatz(27), 111)

    def test_collatz_97(self):
        self.assertEqual(collatz(97), 118)

    def test_collatz_871(self):
        self.assertEqual(collatz(871), 178)

    def test_collatz_6171(self):
        self.assertEqual(collatz(6171), 261)

