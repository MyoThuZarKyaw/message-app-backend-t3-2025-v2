# test_calculator.py

import unittest
from .utils import add, sub, multi, div


class TestCalculatorFunctions(unittest.TestCase):

    def test_add(self):
        """Test the add function with various inputs."""
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)
        self.assertEqual(add(0, 0), 0)

    def test_sub(self):
        """Test the sub function with various inputs."""
        self.assertEqual(sub(5, 3), 2)
        self.assertEqual(sub(3, 5), -2)
        self.assertEqual(sub(0, 0), 0)
        self.assertEqual(sub(-1, -1), 0)

    def test_multi(self):
        """Test the multi function with various inputs."""
        self.assertEqual(multi(2, 3), 6)
        self.assertEqual(multi(-1, 1), -1)
        self.assertEqual(multi(-1, -1), 1)
        self.assertEqual(multi(0, 5), 0)

    def test_div(self):
        """Test the div function with various inputs, including zero division."""
        self.assertEqual(div(6, 3), 2.0)
        self.assertEqual(div(5, 2), 2.5)
        self.assertEqual(div(-6, 3), -2.0)

    def test_div_by_zero(self):
        """Ensure div raises a ZeroDivisionError when dividing by zero."""
        with self.assertRaises(ZeroDivisionError):
            div(1, 0)


if __name__ == '__main__':
    unittest.main()