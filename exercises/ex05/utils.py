"""List utility functions for EX05."""

__author__: str = "730573848"


def only_evens(xs: list[int]) -> list[int]:
    """Retuen a list containing only the even integers from the input list."""
    result: list[int] = []
    for x in xs:
        if x % 2 == 0
            result.append(x)
    return result

def sub(xs: list[int], start: int, end: int) -> list[int]:
    """Return a list which is a subset of the input list between start and end - 1."""
    result: list[int] = []
    
    # Handle out-of-bound indices
    if start < 0:
        start = 0
    if end > len(xs):
        end = len(xs)
    
    # Return an empty list if start is greater than the length or end is <= 0
    if len(xs) == 0 or start >= len(xs) or end <= 0:
        return result
    
    for i in range(start, end):
        result.append(xs[i])
    
    return result

def add_at_index(xs: list[int], value: int, index: int) -> None:
    """Modify the input list by adding a value at the specified index."""
    if index < 0 or index > len(xs):
        raise IndexError("Index is out of bounds for the input list")
    
    # Shift elements to the right to make space for the new value
    xs.append(0)  # Temporary element at the end to make space
    for i in range(len(xs) - 1, index, -1):
        xs[i] = xs[i - 1]  # Shift elements to the right
    
    xs[index] = value
