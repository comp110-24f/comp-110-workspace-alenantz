"""Unit tests for list utility function in utils.py."""

__author__: str = "730573848"

import pytest
from exercises.ex05.utils import only_evens, sub, add_at_index


def test_only_evens_edge_case_empty():
    """Test only_evens with an empty list."""
    assert only_evens([]) == []


def test_only_evens_use_case_all_odds():
    """Test only_evens with a list of all odd numbers."""
    assert only_evens([1, 3, 5]) == []


def test_only_evens_use_case_mixed():
    """Test only_evens with a list of mixed even and odd numbers."""
    assert only_evens([1, 2, 3, 4]) == [2, 4]


def test_sub_edge_case_empty():
    """Test sub with an empty list."""
    assert sub([], 1, 3) == []


def test_sub_use_case_full_range():
    """Test sub with a start and end index covering the full list."""
    assert sub([10, 20, 30, 40], 0, 4) == [10, 20, 30, 40]


def test_sub_use_case_partial_range():
    """Test sub with a start and end index covering a partial range."""
    assert sub([10, 20, 30, 40], 1, 3) == [20, 30]


def test_add_at_index_edge_case_index_out_of_bounds():
    """Test add_at_index with an index out of bounds."""
    with pytest.raises(IndexError):
        add_at_index([1, 2, 3], 4, 5)


def test_add_at_index_use_case_middle():
    """Test add_at_index by adding an element in the middle of the list."""
    l = [1, 2, 3, 5]
    add_at_index(l, 4, 3)
    assert l == [1, 2, 3, 4, 5]


def test_add_at_index_use_case_start():
    """Test add_at_index by adding an element at the start of the list."""
    l = [2, 3, 4]
    add_at_index(l, 1, 0)
    assert l == [1, 2, 3, 4]
