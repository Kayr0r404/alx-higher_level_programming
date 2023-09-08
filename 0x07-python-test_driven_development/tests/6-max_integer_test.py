
import random
import sys
import unittest
max_integer = __import__("6-max_integer").max_integer


class test_max_integer(unittest.TestCase):
    "Test class fo the max_integer function"
    def test_docmodule_string(self):
        moduleDoc = __import__('6-max_integer').__doc__
        self.assertTrue(len(moduleDoc) > 1)
    
    def test_docfunction_string(self):
        functionDoc = __import__('6-max_integer').max_integer.__doc__
        self.assertTrue(len(functionDoc) > 1)

    def test_empty_list(self):
        """Test empty list"""
        results = max_integer([])
        self.assertIsNone(results)
        self.assertIsNone(max_integer([]), None)
        self.assertIsNone(max_integer([None]), None)
        self.assertIsNone(max_integer(), None)

    def test_one_element(self):
        """Test one element"""
        results = max_integer([1])
        self.assertEqual(results, 1)

    def test_mixed_int(self):
        """Test one element"""
        results = max_integer([1, 4, -6, 90, -4000, 0])
        self.assertEqual(results, 90)
    
    def test_lists(self):
        self.assertEqual(max_integer([[1, 2], [1, 3]]), [1, 3])
    
    def test_strings_lists(self):
        self.assertEqual(max_integer(['q', 'w', 'e', 'r', 't', 'y']), 'y')

    def test_same_elements(self):
        """Test one element"""
        results = max_integer([1, 1, 1, 1, 1, 1])
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
