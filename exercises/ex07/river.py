__author__: str = "730573848"

"""File to define River class."""

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear


class River:
    """Class to represent a River with Fish and Bears."""

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []

        # Populate the river with fish and bears
        for _ in range(num_fish):
            self.fish.append(Fish())
        for _ in range(num_bears):
            self.bears.append(Bear())

    def view_river(self):
        """Visualize the current state of the river."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")

    def one_river_day(self):
        """Simulate one day of life in the river."""
        self.day += 1
        for fish in self.fish:
            fish.one_day()
        for bear in self.bears:
            bear.one_day()
        self.bears_eating()
        self.check_hunger()
        self.check_ages()
        self.repopulate_fish()
        self.repopulate_bears()
        self.view_river()

    def one_river_week(self):
        """Simulate one week of life in the river."""
        for _ in range(7):
            self.one_river_day()

    def check_ages(self):
        """Remove any Fish older than 3 days and Bears older than 5 days."""
        self.fish = [fish for fish in self.fish if fish.age <= 3]
        self.bears = [bear for bear in self.bears if bear.age <= 5]

    def remove_fish(self, amount: int):
        """Remove a specified number of fish from the river."""
        self.fish = self.fish[amount:]

    def bears_eating(self):
        """Simulate bears eating fish."""
        for bear in self.bears:
            if len(self.fish) >= 3:
                self.remove_fish(3)
                bear.eat(3)

    def check_hunger(self):
        """Remove any Bears with a hunger score less than 0."""
        self.bears = [bear for bear in self.bears if bear.hunger_score >= 0]

    def repopulate_bears(self):
        """Repopulate the river with new Bears."""
        num_new_bears = len(self.bears) // 2
        self.bears.extend(Bear() for _ in range(num_new_bears))

    def repopulate_fish(self):
        """Repopulate the river with new Fish."""
        num_new_fish = (len(self.fish) // 2) * 4
        self.fish.extend(Fish() for _ in range(num_new_fish))
