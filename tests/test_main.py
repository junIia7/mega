import unittest
from main import main_function

class TestMain(unittest.TestCase):
    def test_addition(self):
        result = main_function(2, 3, '+')
        self.assertEqual(result, 5)

    def test_subtraction(self):
        result = main_function(10, 5, '-')
        self.assertEqual(result, 5)

    def test_multiplication(self):
        result = main_function(4, 3, '*')
        self.assertEqual(result, 12)

    def test_division(self):
        result = main_function(10, 2, '/')
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()