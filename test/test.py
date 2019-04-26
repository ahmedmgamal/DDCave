import unittest
from unittest import TestCase

def exsum(a, b):
    # A comment of a exsum
    return a + b


def exdiff(a, b):
    return a - b



class ExTestCase(TestCase):
    def test_exsum(self):
        self.assertEqual(exsum(3,2), 5)


        
        
        
class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 5, "Should be 5")

if __name__ == '__main__':
    unittest.main()
