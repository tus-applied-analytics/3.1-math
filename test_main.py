# -*- coding: utf-8 -*-
from main import *
import numpy as np
import unittest

class TestAll(unittest.TestCase):
    def test_assignment1(self):
        self.assertEqual(assignment1(1000), 1080)
        self.assertEqual(assignment1(2132), 2302.56)
        self.assertEqual(assignment1(52443), 56638.44)

    def test_assignment2(self):
        self.assertEqual(assignment2(10., 1), 10.)
        self.assertEqual(assignment2(8, 43), 680564733841876926926749214863536422912)
        self.assertEqual(assignment2(16, -1), 0.0625)

    def test_assignment3(self):
        self.assertEqual(assignment3(1.), 2.)
        self.assertTrue(np.allclose(assignment3(0.1), 2.5937424601000023))
        self.assertTrue(np.allclose(assignment3(0.01), 2.7048138294215285))

if __name__ == "__main__":
    unittest.main()
