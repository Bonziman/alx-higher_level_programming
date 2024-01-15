#!/usr/bin/python3


import unittest
from models.rectangle import Rectangle

class TestInit(unittest.TestCase):

    def test_init(self):

        r1 = Rectangle(10, 2)
        self.assertAlmostEqual(r1.id, 1)
        r2 = Rectangle(1, 19)
        self.assertAlmostEqual(r2.id, 2)
        r3 = Rectangle(10, 2, 2, 2, 25)
        self.assertAlmostEqual(r3.id, 25)
        self.assertAlmostEqual(r3.width, 10)
        self.assertAlmostEqual(r3.height, 2)
        self.assertAlmostEqual(r3.x, 2)
        self.assertAlmostEqual(r3.y, 2)
        r3.width = 5
        self.assertAlmostEqual(r3.width, 5)
