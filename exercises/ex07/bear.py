__author__: str = "730573848"


"""File to define Bear class."""


class Bear:
    """Class to represent a Bear with attributes age and hunger_score."""

    def __init__(self):
        """Initialize a Bear with age 0 and hunger_score 0."""
        self.age = 0
        self.hunger_score = 0

    def one_day(self):
        """Simulate one day passing for the Bear."""
        self.age += 1
        self.hunger_score -= 1

    def eat(self, num_fish: int):
        """Increase the Bear's hunger_score by the number of fish eaten."""
        self.hunger_score += num_fish
