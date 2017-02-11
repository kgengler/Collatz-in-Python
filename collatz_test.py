#!/usr/bin/env py.test --pep8

import unittest
import collatz as c


class CollatzTest(unittest.TestCase):

    def test_hotpo_even(self):
        self.assertEqual(c.hotpo(20), 10)

    def test_hotpo_odd(self):
        self.assertEqual(c.hotpo(7), 22)

    def test_collatz_1(self):
        self.assertEqual(c.collatz(1), 0)

    def test_collatz_2(self):
        self.assertEqual(c.collatz(2), 1)

    def test_collatz_9(self):
        self.assertEqual(c.collatz(9), 19)

    def test_collatz_27(self):
        self.assertEqual(c.collatz(27), 111)

    def test_collatz_97(self):
        self.assertEqual(c.collatz(97), 118)

    def test_collatz_871(self):
        self.assertEqual(c.collatz(871), 178)

    def test_collatz_6171(self):
        self.assertEqual(c.collatz(6171), 261)
