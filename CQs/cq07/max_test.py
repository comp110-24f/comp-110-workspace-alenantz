__author__: str = "730573848"

import unittest
from typing import List
from find_max import find_and_remove_max


class TestFindAndRemoveMax(unittest.TestCase):

    def test_expected_value(self) -> None:
        """Test case where the function returns the correct maximum value."""
        lst: List[int] = [5, 1, 8, 3]
        result: int = find_and_remove_max(lst)
        self.assertEqual(result, 8)  # Max value is 8

    def test_mutate_input(self) -> None:
        """Test case where the function mutates the list as expected."""
        lst: List[int] = [2, 2, 5, 5, 5]
        find_and_remove_max(lst)
        self.assertEqual(lst, [2, 2])  # All 5s should be removed

    def test_empty_list(self) -> None:
        """Edge case: when the list is empty."""
        lst: List[int] = []
        result: int = find_and_remove_max(lst)
        self.assertEqual(result, -1)  # Return -1 for empty list
        self.assertEqual(lst, [])  # List remains unchanged


if __name__ == "__main__":
    unittest.main()
