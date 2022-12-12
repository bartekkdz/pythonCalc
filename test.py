import unittest

from C:\Users\dziwirekb\PycharmProjects\pythonProject\main.py import Calculator

class TestSum(unittest.TestCase):

    def test_add(self):
        self.assertEqual(Calculator.add(7,8), 15, "Should be 15")

    def test_sub(self):
        self.assertEqual(Calculator.sub(15,1), 14, "Should be 14")

    def test_mult(self):
        self.assertEqual(Calculator.mult(7, 8), 56, "Should be 56")

    def test_(self):
        self.assertEqual(Calculator.div(52, 4), 13, "Should be 13")
