import unittest
from random_number_handler import main


class TestRandomHandler(unittest.TestCase):

    def test_limits(self):
        lower = 1
        upper = 5
        for _ in range(10):
            result = main({'lower': lower, 'upper': upper}, {})
            result = result['result']
            self.assertTrue(lower <= result < upper)


if __name__ == '__main__':
    unittest.main()
