#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_max_integer(self):
        self.assertAlmostEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertAlmostEqual(max_integer([]), None)
        self.assertAlmostEqual(max_integer([24, 15, 64, 12, 125, 80, 213, 13]), 213)
        self.assertAlmostEqual(max_integer([5,]), 5)
        self.assertAlmostEqual(max_integer([-3, -13, -1, -18]), -1)
        self.assertAlmostEqual(max_integer([-50, -600, -2343, 2234, 1242, 123, 312, 434, 646, 76, -45, 345, -34]), 2234)
