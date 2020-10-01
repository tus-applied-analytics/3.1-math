# -*- coding: utf-8 -*-
from main import main
import unittest

class TestCase(unittest.TestCase):
    def test_main(self):
        self.assertEqual(main(), "Hello world!")

if __name__ == "__main__":
    unittest.main()
