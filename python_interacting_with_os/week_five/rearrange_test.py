#!/usr/bin/env python3

# Writing Unit Tests in Python
# from keyword imports a function from a script
# function can be called with out the need to write the module each time it's called

from rearrange import rearrange_name

# unittest module includes classes and methods for creating unit tests
import unittest

# Include the class we want to inherit in parenthesis
class TestRearrange(unittest.TestCase):
    def test_basic(self):
        testcase = "Lovelace, Ada"
        expected = "Ada Lovelace"
        self.assertEqual(rearrange_name(testcase), expected)

    # test edge case
    def test_empty(self):
        testcase = ""
        expected = ""
        self.assertEqual(rearrange_name(testcase), expected)

    def test_double(self):
        testcase = "Hopper, Grace M."
        expected = "Grace M. Hopper"
        self.assertEqual(rearrange_name(testcase), expected)

    def test_single(self):
        testcase = "Voltaire"
        expected = "Voltaire"
        self.assertEqual(rearrange_name(testcase), expected)


unittest.main()
