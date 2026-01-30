import unittest
from main import calculate

class TestCalculator(unittest.TestCase):
    def test_valid_operations(self):
        self.assertEqual(calculate('+', 5, 3), 8)
        self.assertEqual(calculate('-', 10, 4), 6)
        self.assertEqual(calculate('*', 7, 3), 21)
        self.assertEqual(calculate('/', 15, 5), 3.0)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculate('/', 10,而不0)

    def test_invalid_operator(self):
        with self.assertRaises(ValueError):
            calculate('%', 8, 4)
        with self.assertRaises(ValueError):
            calculate('xyz', 2, 3)

if __name__ == '__main__':
    unittest.main()