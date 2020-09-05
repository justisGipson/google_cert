Unit Test Cheat-Sheet
---------------------

* * * * *

Frankly, the unit testing library for Python is fairly well documented, but it can be a bit of a dry read. Instead, we suggest covering the core module concepts, and then reading in more detail later.

### Best of Unit Testing Standard Library Module

Understand a Basic Example:

-   [https://docs.python.org/3/library/unittest.html\#basic-example](https://docs.python.org/3/library/unittest.html#basic-example)

Understand how to run the tests using the Command Line:

-   [https://docs.python.org/3/library/unittest.html\#command-line-interface](https://docs.python.org/3/library/unittest.html#command-line-interface)

Understand various Unit Test Design Patterns:

-   [https://docs.python.org/3/library/unittest.html\#organizing-test-code](https://docs.python.org/3/library/unittest.html#organizing-test-code)

-   Understand the uses of setUp, tearDown; setUpModule and tearDownModule

Understand basic assertions:

|**Method**|**Checks that**|**New in**|
|:---------|:--------------|:---------|
|[assertEqual(a, b)](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertEqual)|a == b||
|[assertNotEqual(a, b)](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertNotEqual)|a != b||
|[assertTrue(x)](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertTrue)|bool(x) is True||
|[assertFalse(x)](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertFalse)|bool(x) is False||
|[assertIs(a, b)](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIs)|a is b|3.1|
|[assertIsNot(a, b)](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIsNot)|a is not b|3.1|
|[assertIsNone(x)](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIsNone)|x is None|3.1|
|[assertIsNotNone(x)](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIsNotNone)|x is not None|3.1|
|[assertIn(a, b)](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIn)|a in b|3.1|
|[assertNotIn(a, b)](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertNotIn)|a not in b|3.1|
|[assertIsInstance(a, b)](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIsInstance)|isinstance(a, b)|3.2|
|[assertNotIsInstance(a, b)](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertNotIsInstance)|not isinstance(a, b)|3.2|

Understand more specific assertions such as assertRaises

-   [https://docs.python.org/3/library/unittest.html\#unittest.TestCase.assertRaises](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertRaises)

