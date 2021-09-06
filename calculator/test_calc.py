from calc import Calculator
import unittest

calculator = Calculator()

class TestCalculator(unittest.TestCase):

    def test_add(self):
        return self.assertEqual(calculator.add(2, 2), 4)

    def test_subtract(self):
        return self.assertEqual(calculator.subtract(10, 5), 5)

    def test_multiply(self):
        return self.assertEqual(calculator.multiply(10, 5), 50)

    def test_divide(self):
        return self.assertEqual(calculator.divide(10, 5), 2)

if __name__ == '__main__':
    unittest.main()