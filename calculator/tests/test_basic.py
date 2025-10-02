from calculator.app.basic import add, mul, div
import unittest

class TestBasic(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(4, 3, 2, 1), 10.0, "Should be 10.0")
        self.assertEqual(add(30, 20), 50.0, "Should be 50.0")
        return None

    def test_mul(self):
        self.assertEqual(mul(4, 3, 2), 24.0, "Should be 24.0")
        return None

    def test_div(self):
        self.assertEqual(div(4, 3), 1.333, "Should be 1.333")
        return None

# Namespace Trick
if __name__ == "__main__":
    unittest.main()