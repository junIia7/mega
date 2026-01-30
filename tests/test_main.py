import unittest
from main import calculate


class TestCalculator(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(calculate(5, "+", 3), 8)
        self.assertEqual(calculate(-1, "+", 5), 4)
        self.assertEqual(calculate(0, "+", 0), 0)
        self.assertEqual(calculate(2.5, "+", 3.5), 6.0)

    def test_subtraction(self):
        self.assertEqual(calculate(10, "-", 4), 6)
        self.assertEqual(calculate(3, "-", 7), -4)
        self.assertEqual(calculate(0, "-", 5), -5)
        self.assertEqual(calculate(-2, "-", -3), 1)

    def test_multiplication(self):
        self.assertEqual(calculate(7, "*", 3), 21)
        self.assertEqual(calculate(-4, "*", 5), -20)
        self.assertEqual(calculate(0, "*", 100), 0)
        self.assertEqual(calculate(2.5, "*", 4), 10.0)

    def test_division(self):
        self.assertEqual(calculate(15, "/", 5), 3.0)
        self.assertEqual(calculate(10, "/", 2), 5.0)
        self.assertEqual(calculate(1, "/", 2), 0.5)
        self.assertEqual(calculate(-10, "/", 2), -5.0)
        self.assertEqual(calculate(5, "/", 2), 2.5)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculate(10, "/", 0)
        with self.assertRaises(ZeroDivisionError):
            calculate(0, "/", 0)

    def test_invalid_operator(self):
        with self.assertRaises(ValueError):
            calculate(8, "%", 4)
        with self.assertRaises(ValueError):
            calculate(2, "xyz", 3)
        with self.assertRaises(ValueError):
            calculate(5, "", 3)
        with self.assertRaises(ValueError):
            calculate(5, None, 3)

    def test_invalid_operand_type(self):
        with self.assertRaises(TypeError):
            calculate("a", "+", 3)
        with self.assertRaises(TypeError):
            calculate(2, "*", "b")


if __name__ == "__main__":
    unittest.main()