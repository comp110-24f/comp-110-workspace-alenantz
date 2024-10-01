"""Plan a Tea Party"""

__author__: str = "730573848"


def main_planner(guests: int) -> None:
    """Connecting all the below functions using the main function"""
    print(f"A Cozy Tea Party for {guests} People!")

    """Calculate the number of tea bags needed"""

    print((f"Tea Bags: {tea_bags(guests)}"))

    """Calculate the number of treats needed"""

    print((f"Treats: {treats(guests)}"))

    """Calculate the total cost"""
    print(f"Cost: ${cost(tea_bags(guests), treats(guests))}")


# main_planner function to string all the below functions together and calculate based on the number of guests I input.
# had to use the f and {} to signify my previous function values to run in my main planner as a single function.
# used the print function to report the title of the values Im using my functions to calculate.
# I implemented all of the variables i needed and just assigned my number of guests to each to report the correct value.


def tea_bags(people: int) -> int:
    """Calculates the number of teabags per guest"""
    return people * 2


# had to calculate the number of tea bags per person by accounting that each person would want 2 teabags.


def treats(people: int) -> int:
    """Computing the number of treats needed"""
    return int(tea_bags(people=people) * 1.5)


# had to add the connection of tea_bags to the new treats function. Because people was the recorded value i had to use that to collect into one value.


def cost(tea_count: int, treat_count: int) -> float:
    """Computing the cost of teabags and treats combined"""
    return tea_count * 0.50 + treat_count * 0.75


# had to name the values of tea and treats to allow the calculation of the number of treats and tea bags into one value.

if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
# this allows for the main planner function to read the whole document and allow for the function to ask for how many people are attending to make its calculation.
# also had to add that guests is an int value.
