__author__: str = "730573848"


def find_and_remove_max(lst: list[int]) -> int:
    if not lst:  # Check if the list is empty
        return -1

    max_value = max(lst)  # Find the maximum value in the list

    # Remove all instances of the maximum value
    while max_value in lst:
        lst.remove(max_value)

    return max_value
