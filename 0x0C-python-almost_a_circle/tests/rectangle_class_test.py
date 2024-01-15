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
        with self.assertRaises(TypeError):
            r4 = Rectangle("School", 1)
            r5 = Rectangle(1, "School")
            r6 = Rectangle([1, 2, 3], 3)
            r7 = Rectangle(1, [1, 2, 3])
        with self.assertRaises(ValueError):
            r8 = Rectangle(-5, 5, 4, 1, 12)
            r9 = Rectangle(0, 5, 4, 1, 13)
            r10 = Rectangle(1, -1, 4, 3, 14)
            r11= Rectangle(1, 0, 4, 3, 15)
            r11 = Rectangle(1, 1, -3, 3, 16)
            r12 = rectangle(1, 1, 3, -3, 17)
