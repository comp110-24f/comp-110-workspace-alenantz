"""This module contains utility functions for working with lists of integers."""

__author__: str = "730573848"


def all(input_list: list[int], target: int) -> bool:
    """Check if all elements in the input list are equal to the target integer."""
    if len(input_list) == 0:
        return False  # Return False if the list is empty
    for number in input_list:
        if number != target:
            return False
    return True


def max(input_list: list[int]) -> int:
    """Return the largest integer in the input list."""
    if len(input_list) == 0:
        raise ValueError("max() arg is an empty List")

    current_max: int = input_list[0]  # Initialize with the first element

    for number in input_list:
        if number > current_max:
            current_max = number

    return current_max


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Check if two lists of integers are equal, element by element."""
    if len(list1) != len(list2):
        return False  # If lengths differ, they can't be equal

    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False

    return True


def extend(list1: list[int], list2: list[int]) -> None:
    """Append the elements of the second list to the first list."""
    for number in list2:
        list1.append(number)
