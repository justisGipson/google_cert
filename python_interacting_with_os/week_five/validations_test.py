#!/usr/bin/env python3

import unittest

from validations import validate_users

class TestValidateUsers(unittest.TestCase):
    def test_valid(self):
        self.assertEqual(validate_users("validuser", 3), True)

    def test_too_short(self):
        self.assertEqual(validate_users("inv", 5), False)

    def test_invalid_chars(self):
        self.assertEqual(validate_users("invalid_user", 1), False)

    def test_invalid_minlen(self):
        self.assertRaises(ValueError, validate_users, "user", -1)

unittest.main()
