#!/usr/bin/env py.test --pep8

import unittest
import collatz as c


class CollatzTest(unittest.TestCase):

    def test_hotpo_even(self):
        """assert HOTPO halves an even number"""
        self.assertEqual(c.hotpo(20), 10)

    def test_hotpo_odd(self):
        """assert HOTPO triples and adds 1 to an odd number"""
        self.assertEqual(c.hotpo(7), 22)

    def test_collatz_1(self):
        """assert 1 results in 0 steps"""
        self.assertEqual(c.collatz(1), 0)

    def test_collatz_2(self):
        """assert 2 results in 1 step"""
        self.assertEqual(c.collatz(2), 1)

    def test_collatz_9(self):
        """assert 9 results in 19 steps"""
        self.assertEqual(c.collatz(9), 19)

    def test_collatz_27(self):
        """assert 27 results in 111 steps"""
        self.assertEqual(c.collatz(27), 111)

    def test_collatz_97(self):
        """assert 97 results 118 steps"""
        self.assertEqual(c.collatz(97), 118)

    def test_collatz_871(self):
        """assert 871 results in 178 steps"""
        self.assertEqual(c.collatz(871), 178)

    def test_collatz_6171(self):
        """assert 6171 results in 261 steps"""
        self.assertEqual(c.collatz(6171), 261)
