"""List utility functions for EX05."""

__author__: str = "730573848"


def only_evens(input_list: list[int]) -> list[int]:
    """Return a list containing only the even elements from the input list."""
    result = []
    for num in input_list:
        if num % 2 == 0:
            result.append(num)
    return result


def sub(input_list: list[int], start: int, end: int) -> list[int]:
    """Return a list which is a subset of the input list, between start index and end index-1."""
    result = []
    if len(input_list) == 0 or start >= len(input_list) or end <= 0:
        return result

    if start < 0:
        start = 0
    if end > len(input_list):
        end = len(input_list)

    i = start
    while i < end:
        result.append(input_list[i])
        i += 1

    return result


def add_at_index(input_list: list[int], element: int, index: int) -> None:
    """Insert an element at the specified index in the input list."""
    if index < 0 or index > len(input_list):
        raise IndexError("Index is out of bounds for the input list")

    input_list.append(0)  # Add space at the end of the list
    i = len(input_list) - 1
    while i > index:
        input_list[i] = input_list[i - 1]
        i -= 1
    input_list[index] = element
