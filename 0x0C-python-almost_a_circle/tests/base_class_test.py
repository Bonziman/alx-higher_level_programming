#!/usr/bin/python3
"""Unittest for the base class
"""
import unittest
from models.base import Base


class TestInit(unittest.TestCase):

    def test_init(self):
        b1 = Base()
        self.assertAlmostEqual(b1.id, 1)
        b2 = Base()
        self.assertAlmostEqual(b2.id, 2)
        b3 = Base(15)
        self.assertAlmostEqual(b3.id, 15)
