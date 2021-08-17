import unittest

import paye

class TestCalculator(unittest.TestCase):
    def test_lessThan14000(self):
        tax = paye.lessThan14000(10)
        self.assertEqual(0, tax)

if __name__ == '__main__':
    unittest.main()
