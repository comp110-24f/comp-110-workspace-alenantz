"""Mutating functions."""

__author__: str = "730573848"


def manual_append(list: list[int], item: int) -> None:
    list.append(item)


def double(list: list[int]) -> None:
    index: int = 0
    while index < len(list):
        list[index] *= 2
        index += 1


# Global variables
list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1

# Calling the double function with list_2
double(list_2)

# Print statements
print("list_1:", list_1)
print("list_2:", list_2)
