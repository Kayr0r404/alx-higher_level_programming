
import random
import sys
import unittest
max_integer = __import__("6-max_integer").max_integer


class test_max_integer(unittest.TestCase):
    "Test class fo the max_integer function"

    def test_empty_list(self):
        """Test empty list"""
        results = max_integer([])
        self.assertIsNone(results)

    def test_one_element(self):
        """Test one element"""
        results = max_integer([1])
        self.assertEqual(results, 1)

    def test_main(self):
        """Test long list random avalues"""
        # Smallest integer
        smallest = -sys.maxsize - 1
        # Largest integer
        largest = sys.maxsize
        lists = [[random.randint(smallest, largest)] for _ in range(100000)]
        for i in range(len(lists)):
            self.assertEqual(max_integer(lists[i]), max(lists[i]))


if __name__ == "__main__":
    unittest.main()
