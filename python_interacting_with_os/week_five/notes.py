# Testing in Python

# ==========================================================================================

# Manual Testing
# Running the code via the interpreter to verify that we are getting the results that we want, before using it in our
# script.

# Automatic Testing
# Codifying our tests, so that they will run when our code does. Verifying that we will get the desired results.

# ==========================================================================================

# Unit Tests

# Unit tests are used to verify that small, isolated parts of a program are correct.
# Generally written alongside the code to test the behavior of individual pieces or units, like functions or methods.

# ==========================================================================================

# Edge Cases

# Edge cases are inputs to our code that produce unexpected results, and are found at the extreme ends of the ranges
# of input we imagine our programs will typically work with

# ==========================================================================================

# Other Test Concepts

# White-box testing also sometimes called clear-box or transparent testing relies on the test creators knowledge of
# the software being tested to construct the test cases.

# Black-box testing, the software being tested is treated like an opaque box. In other words, the tester doesn't know
# the internals of how the software works. Black-box tests are written with an awareness of what the program is
# supposed to do, its requirements or specifications, but not how it does it.

# Integration Test

# Integration tests verify that the interactions between the different pieces of code in integrated environments are
# working the way we expect them to. While unit tests shouldn't cross boundaries to do things like make a network
# request or integrate with an API or database, the goal of an integration test is to verify these kinds of
# interactions and make sure the whole system works how you expect it to. Integration test, usually take the
# individual modules of code that unit test verify then combine them into a group to test.

# Smoke Test
# Smoke test sometimes called build verification test, get their name from a concept that comes from testing hardware
# equipment. Plug in the given piece of hardware and see if smoke starts coming out of it. When writing software smoke
# test serve as a kind of sanity check to find major bugs in a program. Smoke test answer basic questions like, does
# the program run? These tests are usually run before more refined testing takes place. Since if the software fails
# the smoke test you can be pretty sure none of the other tests will pass either. As they say where there's smoke
# there's fire. For a web service the smoke test would be to check if there's a service running on the
# corresponding port. For an automation script, the smoke test would be to run it manually with some basic
# input and check that the script finishes successfully.

# Regression Test
# They're usually written as part of a debugging and troubleshooting process to verify that an issue or error has
# been fixed once it's been identified. Say our script has a bug and we're trying to fix it. A good approach to doing
# this would be the first right to test fails by triggering the buggy behavior, then fix the bug so that a test passes.
# Regression tests are useful part of a test suite because they ensure that the same mistake doesn't happen twice.
# The same bug can't be reintroduced into the code because introducing it will cause the regression test to fail

# Load Test
# These tests verify that the system behaves well when it's under significant load. To actually perform these tests
# will need to generate traffic to our application simulating typical usage of the service. These tests can be
# super-helpful when deploying new versions of our applications to verify that performance does not degrade. For
# example, we might want to measure the response time of our website while there are 100 requests per second on our
# pages, or a 1000, or 10,000. The actual numbers will depend on the expectations of how much traffic our website
# will receive.

# Taking together a group of tests of one or many kinds is commonly referred to as a test suite. A good diversity of
# test types can create a more robust test suite that helps ensure your scripts and automation, do what you tell them
# to.

# ==========================================================================================

# Test Driven Development (TDD)

# This calls for the tests to written before the code. Makes for more thoughtful and well-written programs.
# Helps you think about all the ways the code could fail.
# write test -> fails -> write code -> run test -> fix code if it fails...
# increases the time needed to write code, but also decreases the chance for bugs

# More about tests

# https://landing.google.com/sre/sre-book/chapters/monitoring-distributed-systems/
# https://landing.google.com/sre/sre-book/chapters/testing-reliability/
# https://testing.googleblog.com/2007/10/performance-testing.html
# https://www.guru99.com/smoke-testing.html
# https://www.guru99.com/exploratory-testing.html
# https://testing.googleblog.com/2008/09/test-first-is-fun_08.html

# ==========================================================================================

# Errors and Exceptions

#
