#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        self.assertEqual(max_integer([1,2]), 2)
        self.assertEqual(max_integer([0, 0]), 0)
        self.assertEqual(max_integer([-1,-2]), -1)
    def test_empty_list(self):
        self.assertIsNone(max_integer([]))