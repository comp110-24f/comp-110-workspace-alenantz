__author__: str = "730573848"
# visualize.py

# Import the concat function from concatenation.py
from concatenation import concat
from coordinates import get_coords


# Global variables
x = "123"
y = "abc"

# Call the concat function and print the result
print(concat(x, y))

# Call the get_coords function with x and y
get_coords(x, y)
