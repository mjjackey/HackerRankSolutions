import unittest
from test1 import unique_substring_num

class TestCountUniqueSubstrings(unittest.TestCase):
    def test_happy_path(self):
        self.assertEqual(unique_substring_num("abcabc", 3), 3)
        self.assertEqual(unique_substring_num("aaaa", 2), 1)
        self.assertEqual(unique_substring_num("abcdefg", 4), 4)
        self.assertEqual(unique_substring_num("abcabcabc", 2), 3)

    def test_edge_cases(self):
        self.assertEqual(unique_substring_num("", 1), 0)
        self.assertEqual(unique_substring_num("a", 0), 1)
        self.assertEqual(unique_substring_num("a", 1), 1)
        self.assertEqual(unique_substring_num("a", 2), 0)
        self.assertEqual(unique_substring_num("abc", 3), 1)
        self.assertEqual(unique_substring_num("abc", 4), 0)
        self.assertEqual(unique_substring_num("abcabcabc", 9), 1)
        self.assertEqual(unique_substring_num("abcabcabc", 10), 0)

if __name__ == '__main__':
    unittest.main()