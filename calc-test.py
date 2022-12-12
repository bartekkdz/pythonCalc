import unittest
from main import Calculator

class TestSum(unittest.TestCase):

    def test_add(self):
        #given
        a = 7
        b = 8
        #when
        expected = 15
        typ = type(expected)
        #then
        result = Calculator.add(a,b)
        self.assertEqual(type(result), typ, "wrong type of result")
        self.assertEqual(result, expected, "Should be 15")

    def test_sub(self):
        #given
        a = 15
        b = 1
        #when
        expected = 14
        typ = type(expected)
        #then
        result = Calculator.sub(a,b)
        self.assertEqual(type(result), typ, "wrong type of result")
        self.assertEqual(result, expected, "Should be 14")

    def test_mult(self):
        #given
        a = 7
        b = 8
        #when
        expected = 56
        typ = type(expected)
        #then
        result = Calculator.mult(a,b)
        self.assertEqual(type(result), typ, "wrong type of result")
        self.assertEqual(result, expected, "Should be 56")

    def test_div(self):
        #given
        a = 52
        b = 4
        #when
        expected = 13
        typ = type(expected)
        #then
        result = Calculator.div(a,b)
        self.assertEqual(type(result), float, "wrong type of result")
        self.assertEqual(result, expected, "Should be 13")

unittest.main(argv=[''], verbosity=2, exit=False)