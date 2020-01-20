#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

def test_max_last(self):
        self.assertEqual(max_integer([1, 1, 1, 8]), 8)
    
    def test_max_one_elem(self):
        self.assertEqual(max_integer([70]), 70)

    def test_max_mid(self):
        self.assertEqual(max_integer([0, 7]), 7)

    def test_max_one_negative(self):
        self.assertEqual(max_integer([-1, 0, 73, 80]), 80)

    def test_max_all_negative(self):
        self.assertEqual(max_integer([-1, -82, -43, -45]), -1)

    def test_max_empty_list(self):
        self.assertEqual(max_integer([]), None)

if __name__ == '__main__':
    unittest.main()
