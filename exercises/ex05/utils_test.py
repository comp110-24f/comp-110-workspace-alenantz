"""Unit tests for list utility function in utils.py."""

__author__: str = "730573848"

import unittest
from exercises.ex05.utils import only_evens


class TestOnlyEvens(unittest.TestCase):
    """Tests for the only_evens function."""

    def test_only_evens_with_mixed_numbers(self):
        """Test only_evens with a mix of even and odd numbers."""
        self.assertEqual(only_evens([1, 2, 3]), [2])

    def test_only_evens_with_all_odd_numbers(self):
        """Test only_evens with a list of all odd numbers."""
        self.assertEqual(only_evens([1, 5, 3]), [])

    def test_only_evens_with_all_even_numbers(self):
        """Test only_evens with a list of all even numbers."""
        self.assertEqual(only_evens([4, 4, 4]), [4, 4, 4])

    def test_only_evens_with_empty_list(self):
        """Test only_evens with an empty list."""
        self.assertEqual(only_evens([]), [])


if __name__ == "__main__":
    unittest.main()

import unittest
from exercises.ex05.utils import sub


class TestSub(unittest.TestCase):
    """Tests for the sub function."""

    def test_sub_normal_case(self):
        """Test sub with normal start and end indices."""
        self.assertEqual(sub([10, 20, 30, 40], 1, 3), [20, 30])

    def test_sub_negative_start(self):
        """Test sub with a negative start index."""
        self.assertEqual(sub([10, 20, 30, 40], -1, 3), [10, 20, 30])

    def test_sub_end_greater_than_length(self):
        """Test sub with end index greater than the length of the list."""
        self.assertEqual(sub([10, 20, 30, 40], 1, 6), [20, 30, 40])

    def test_sub_empty_list(self):
        """Test sub with an empty list."""
        self.assertEqual(sub([], 1, 3), [])

    def test_sub_start_greater_than_length(self):
        """Test sub with start index greater than or equal to the length of the list."""
        self.assertEqual(sub([10, 20, 30], 3, 5), [])
