"""Plan a Tea Party"""

_author_: str = 730573848


def main_planner(guests: int) -> None:
    """Connecting all the below functions using the main function"""
    print(f"A Cozy Tea Party for {guests} People!")

    """Calculate the number of tea bags needed"""
    num_tea_bags = tea_bags(guests)
    print((f"Tea Bags: {num_tea_bags}"))

    """Calculate the number of treats needed"""
    num_treats = treats(guests)
    print((f"Treats: {num_treats}"))

    """Calculate the total cost"""
    total_cost = cost(tea_count=num_tea_bags, treat_count=num_treats)  # type: ignore
    print((f"Cost: ${total_cost: .2f}"))


# main_planner function to string all the below functions together and calculate based on the number of guests I input.
# had to use the f and {} to signify my previous function values to run in my main planner as a single function.
# used the print function to report the title of the values Im using my functions to calculate.


def tea_bags(people: int) -> int:
    """Calculates the number of teabags per guest"""
    tea_bags = people * 2
    return int(tea_bags)


# had to calculate the number of tea bags per person by accounting that each person would want 2 teabags.


def treats(people: int) -> int:
    """Computing the number of treats needed"""
    num_tea_bags = tea_bags(people=people)
    num_treats = num_tea_bags * 1.5
    return int(num_treats)


# had to add the connection of tea_bags to the new treats function. Because people was the recorded value i had to use that to collect into one value.


def cost(tea_count: int, treat_count: int) -> float:
    """Computing the cost of teabags and treats combined"""
    tea_cost = tea_count * 0.50
    treat_cost = treat_count * 0.75
    total_cost = tea_cost + treat_cost
    return total_cost


# had to name the values of tea and treats to allow the calculation of the number of treats and tea bags into one value.

if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
# this allows for the main planner function to read the whole document and allow for the function to ask for how many people are attending to make its calculation.
# also had to add that guests is an int value.
