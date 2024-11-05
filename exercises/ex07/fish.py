__author__: str = "730573848"


"""File to define Fish class."""


class Fish:
    """Class to represent a Fish with attribute age."""

    def __init__(self):
        """Initialize a Fish with age 0."""
        self.age = 0

    def one_day(self):
        """Simulate one day passing for the Fish."""
        self.age += 1
