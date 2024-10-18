"""Summing the elements of a list using different loops"""

__author__: str = "730573848"


# Part 1: w_sum function using a while loop
def w_sum(vals: list[float]) -> float:
    total = 0.0
    i = 0
    while i < len(vals):
        total += vals[i]
        i += 1
    return total


# Part 2: f_sum function using a for... in... loop (without range)
def f_sum(vals: list[float]) -> float:
    total = 0.0
    for val in vals:
        total += val
    return total


# Part 3: f_range_sum function using a for ... in range(...) loop
def f_range_sum(vals: list[float]) -> float:
    total = 0.0
    for i in range(len(vals)):
        total += vals[i]
    return total
