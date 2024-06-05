import unittest

def product(a, b):
    total = 0
    for i in range(a):
        total += b
    return total

class TestProduct(unittest.TestCase):
    def test_multiplies_two_numbers_together(self):
        self.assertEqual(
            product(3, 5), 15
        )

if __name__ == "__main__":
    unittest.main()