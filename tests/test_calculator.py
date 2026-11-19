import unittest

from calculator import add, multiply, subtract


class CalculatorTests(unittest.TestCase):
    def test_add_returns_sum(self):
        self.assertEqual(add(3, 4), 7)

    def test_subtract_integers(self):
        self.assertEqual(subtract(9, 4), 5)

    def test_subtract_fractional_operands(self):
        self.assertEqual(subtract(5.5, 2), 3.5)

    def test_subtract_negative_result(self):
        self.assertEqual(subtract(3, 8), -5)

    def test_subtract_zero_operands(self):
        self.assertEqual(subtract(0, 0), 0)

    def test_multiply_integers(self):
        self.assertEqual(multiply(3, 4), 12)

    def test_multiply_fractional_operands(self):
        self.assertEqual(multiply(1.5, 2), 3.0)

    def test_multiply_by_zero(self):
        self.assertEqual(multiply(7, 0), 0)

    def test_multiply_negative_operand(self):
        self.assertEqual(multiply(-3, 4), -12)

    def test_multiply_two_negative_operands(self):
        self.assertEqual(multiply(-3, -4), 12)


if __name__ == "__main__":
    unittest.main()
